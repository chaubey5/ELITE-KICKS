from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from decimal import Decimal
from .models import Shoe, Brand, Category, Review, Cart, CartItem, Size, Color, Order, OrderItem, Wishlist

# --- AUTH SYSTEM (ELITE ACCESS) ---
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    return render(request, 'shoes/register.html', {'form': UserCreationForm()})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    return render(request, 'shoes/login.html', {'form': AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('home')

# --- CORE SHOP PAGES ---
def home(request):
    # Featured specimens for the landing hub
    featured = Shoe.objects.filter(is_available=True).annotate(avg_rating=Avg('reviews__rating'))[:6]
    return render(request, 'shoes/home.html', {
        'featured_shoes': featured, 
        'brands': Brand.objects.all(), 
        'categories': Category.objects.all()
    })

def shop(request):
    shoes = Shoe.objects.filter(is_available=True).annotate(avg_rating=Avg('reviews__rating'))
    paginator = Paginator(shoes, 12)
    return render(request, 'shoes/shop.html', {
        'shoes': paginator.get_page(request.GET.get('page')), 
        'brands': Brand.objects.all(), 
        'categories': Category.objects.all()
    })

def shoe_detail(request, shoe_id):
    shoe = get_object_or_404(Shoe, id=shoe_id)
    reviews = shoe.reviews.all()
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    in_wishlist = request.user.is_authenticated and Wishlist.objects.filter(user=request.user, shoe=shoe).exists()
    return render(request, 'shoes/shoe_detail.html', {
        'shoe': shoe, 'reviews': reviews, 'average_rating': avg_rating, 
        'in_wishlist': in_wishlist, 'sizes': shoe.sizes.all(), 'colors': shoe.colors.all()
    })

def search(request):
    query = request.GET.get('q')
    shoes = Shoe.objects.filter(name__icontains=query) if query else Shoe.objects.none()
    return render(request, 'shoes/search.html', {'shoes': shoes, 'query': query})

# --- CART ARCHITECTURE ---
def get_or_create_cart(request):
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
    else:
        if not request.session.session_key: request.session.create()
        cart, _ = Cart.objects.get_or_create(session_key=request.session.session_key)
    return cart

def add_to_cart(request, shoe_id):
    if request.method == 'POST':
        cart = get_or_create_cart(request)
        item, created = CartItem.objects.get_or_create(
            cart=cart, shoe_id=shoe_id, 
            size_id=request.POST.get('size'), 
            color_id=request.POST.get('color')
        )
        qty = int(request.POST.get('quantity', 1))
        item.quantity = (item.quantity + qty) if not created else qty
        item.save()
    return redirect('cart')

def update_cart_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    action = request.GET.get('action')
    if action == 'increment': item.quantity += 1
    elif action == 'decrement' and item.quantity > 1: item.quantity -= 1
    item.save()
    return redirect('cart')

def remove_cart_item(request, item_id):
    CartItem.objects.filter(id=item_id).delete()
    return redirect('cart')

def clear_cart(request):
    cart = get_or_create_cart(request)
    cart.items.all().delete()
    return redirect('cart')

def cart_view(request):
    cart = get_or_create_cart(request)
    return render(request, 'shoes/cart.html', {'cart': cart, 'cart_items': cart.items.all()})

# --- SECURE CHECKOUT & LOGISTICS ---
@login_required
def checkout(request):
    cart = get_or_create_cart(request)
    items = cart.items.all()
    if not items: return redirect('cart')
    
    subtotal = sum(i.shoe.price * i.quantity for i in items)
    shipping = Decimal('0.00') if subtotal > 50 else Decimal('9.99')
    total = subtotal + shipping

    if request.method == 'POST':
        city = request.POST.get('city', '').strip()
        if not city:
            messages.error(request, "CRITICAL: City is mandatory for transaction.")
            return redirect('checkout')

        order = Order.objects.create(
            user=request.user,
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            address=request.POST.get('address'),
            city=city,
            state=request.POST.get('state', 'N/A'),
            zip_code=request.POST.get('zip_code', '000000'),
            subtotal=subtotal,
            total_amount=total,
            payment_method=request.POST.get('payment_method')
        )
        for i in items:
            OrderItem.objects.create(order=order, shoe=i.shoe, quantity=i.quantity, price=i.shoe.price)
        
        items.delete() # Clear the terminal cart after authorization
        return redirect('order_confirmation', order_id=order.id)

    return render(request, 'shoes/checkout.html', {
        'cart_items': items, 'total_amount': total, 'subtotal': subtotal, 'shipping': shipping
    })

# --- ORDER DATABASE & HISTORY ---
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'shoes/order_confirmation.html', {'order': order})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'shoes/order_history.html', {'orders': orders})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'shoes/order_detail.html', {'order': order})

# --- EXTRA UTILITIES (FAQ & CONTACT) ---
def faq(request):
    return render(request, 'shoes/faq.html')

def contact(request):
    if request.method == 'POST':
        messages.success(request, "Transmission received. Elite support will contact you shortly.")
        return redirect('home')
    return render(request, 'shoes/contact.html')

@login_required
def wishlist_view(request):
    return render(request, 'shoes/wishlist.html', {'wishlist_items': Wishlist.objects.filter(user=request.user)})

@login_required
def add_to_wishlist(request, shoe_id):
    Wishlist.objects.get_or_create(user=request.user, shoe_id=shoe_id)
    return redirect('shoe_detail', shoe_id=shoe_id)

@login_required
def remove_from_wishlist(request, shoe_id):
    Wishlist.objects.filter(user=request.user, shoe_id=shoe_id).delete()
    return redirect('wishlist')

@login_required
def add_review(request, shoe_id):
    if request.method == 'POST':
        Review.objects.create(user=request.user, shoe_id=shoe_id, rating=request.POST.get('rating'), comment=request.POST.get('comment'))
    return redirect('shoe_detail', shoe_id=shoe_id)

def quick_rate(request, shoe_id):
    return JsonResponse({'status': 'ok'})