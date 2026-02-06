import random
import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from .models import Shoe, Category, Brand, Order, Cart, CartItem, Wishlist

# --- UTILS & SECURITY LOCK ---
def admin_check(user):
    """Checks if the user is both logged in and a staff member."""
    return user.is_authenticated and user.is_staff

# --- PUBLIC VIEWS ---
def home(request):
    shoes = Shoe.objects.filter(is_available=True).order_by('-id')[:8]
    return render(request, 'shoes/home.html', {
        'shoes': shoes, 
        'brands': Brand.objects.all(),
        'categories': Category.objects.all()
    })

def shop(request):
    shoes = Shoe.objects.all().order_by('-id')
    cat_name = request.GET.get('category')
    brand_name = request.GET.get('brand')

    if cat_name: shoes = shoes.filter(category__name=cat_name)
    if brand_name: shoes = shoes.filter(brand__name=brand_name)

    return render(request, 'shoes/shop.html', {
        'shoes': shoes,
        'categories': Category.objects.all(),
        'brands': Brand.objects.all(),
        'selected_category': cat_name,
        'selected_brand': brand_name,
    })

def shoe_detail(request, shoe_id):
    shoe = get_object_or_404(Shoe, id=shoe_id)
    return render(request, 'shoes/shoe_detail.html', {'shoe': shoe})

def men_collection(request):
    shoes = Shoe.objects.filter(is_available=True) 
    return render(request, 'shoes/men_collection.html', {'shoes': shoes})

# --- CART SYSTEM ---
def add_to_cart(request, shoe_id):
    if request.method == 'POST':
        shoe = get_object_or_404(Shoe, id=shoe_id)
        size = request.POST.get('size')
        qty = int(request.POST.get('quantity', 1))

        if request.user.is_authenticated:
            cart, _ = Cart.objects.get_or_create(user=request.user)
        else:
            if not request.session.session_key: 
                request.session.create()
            cart, _ = Cart.objects.get_or_create(session_key=request.session.session_key)

        item, created = CartItem.objects.get_or_create(cart=cart, shoe=shoe, size=size)
        item.quantity = (item.quantity + qty) if not created else qty
        item.save()
    return redirect('cart')

def cart_view(request):
    if request.user.is_authenticated:
        items = CartItem.objects.filter(cart__user=request.user)
    else:
        items = CartItem.objects.filter(cart__session_key=request.session.session_key) if request.session.session_key else []
    
    total = sum(i.get_total_item_price() for i in items)
    return render(request, 'shoes/cart.html', {'cart_items': items, 'total_amount': total})

def update_cart(request, item_id, action):
    item = get_object_or_404(CartItem, id=item_id)
    if action == 'increment': item.quantity += 1
    elif action == 'decrement' and item.quantity > 1: item.quantity -= 1
    item.save()
    return redirect('cart')

def remove_from_cart(request, item_id):
    get_object_or_404(CartItem, id=item_id).delete()
    return redirect('cart')

def clear_cart(request):
    if request.user.is_authenticated:
        CartItem.objects.filter(cart__user=request.user).delete()
    else:
        CartItem.objects.filter(cart__session_key=request.session.session_key).delete()
    return redirect('cart')

# --- CHECKOUT & ORDER ---
def checkout(request):
    if request.user.is_authenticated:
        items = CartItem.objects.filter(cart__user=request.user)
    else:
        items = CartItem.objects.filter(cart__session_key=request.session.session_key)
    total = sum(i.get_total_item_price() for i in items)
    return render(request, 'shoes/checkout.html', {'cart_items': items, 'total_amount': total})

def order_confirmation(request):
    if request.method == 'POST':
        context = {
            'order_id': f"SHOE-{random.randint(10000, 99999)}",
            'date': datetime.datetime.now().strftime("%d %b %Y"),
            'name': request.POST.get('name'),
            'total_amount': request.POST.get('total_amount'),
        }
        return render(request, 'shoes/order_confirmation.html', context)
    return redirect('home')

def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-id') if request.user.is_authenticated else []
    return render(request, 'shoes/order_history.html', {'orders': orders})

# --- ADMIN DASHBOARD & POWERS ---
@user_passes_test(admin_check, login_url='login')
def admin_dashboard(request):
    shoes = Shoe.objects.all().order_by('-id')
    orders = Order.objects.all().order_by('-id')
    all_users = User.objects.all()
    
    total_products = shoes.count()
    total_orders = orders.count()
    total_users = all_users.count()
    total_revenue = orders.aggregate(Sum('total_amount'))['total_amount__sum'] or 0

    context = {
        'shoes': shoes,
        'orders': orders,
        'users': all_users,
        'total_products': total_products,
        'total_orders': total_orders,
        'total_users': total_users,
        'total_revenue': total_revenue,
    }
    return render(request, 'shoes/admin_dashboard.html', context)

@user_passes_test(admin_check, login_url='login')
def add_product_custom(request):
    if request.method == 'POST':
        Shoe.objects.create(
            name=request.POST.get('name'),
            price=request.POST.get('price'),
            description=request.POST.get('description'),
            brand_id=request.POST.get('brand'),
            image=request.FILES.get('image'),
            is_available=True
        )
        return redirect('admin_dashboard')
    return render(request, 'shoes/add_product_custom.html', {'brands': Brand.objects.all()})

@user_passes_test(admin_check, login_url='login')
def update_price(request, shoe_id):
    if request.method == 'POST':
        shoe = get_object_or_404(Shoe, id=shoe_id)
        shoe.price = request.POST.get('new_price')
        shoe.save()
    return redirect('admin_dashboard')

@user_passes_test(admin_check, login_url='login')
def toggle_stock(request, shoe_id):
    shoe = get_object_or_404(Shoe, id=shoe_id)
    shoe.is_available = not shoe.is_available
    shoe.save()
    return redirect('admin_dashboard')

@user_passes_test(admin_check, login_url='login')
def delete_product(request, shoe_id):
    get_object_or_404(Shoe, id=shoe_id).delete()
    return redirect('admin_dashboard')

# --- AUTH SYSTEM ---
def register(request):
    if request.method == 'POST':
        u, p = request.POST.get('username'), request.POST.get('password')
        if not u or not p:
            return render(request, 'shoes/register.html', {'error': 'Required fields missing'})
        if User.objects.filter(username=u).exists():
            return render(request, 'shoes/register.html', {'error': 'Username taken'})
        User.objects.create_user(username=u, password=p)
        return redirect('login')
    return render(request, 'shoes/register.html')

def login_view(request):
    if request.method == 'POST':
        u, p = request.POST.get('username'), request.POST.get('password')
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            return redirect('admin_dashboard' if user.is_staff else 'home')
        return render(request, 'shoes/login.html', {'error': 'Invalid Credentials'})
    return render(request, 'shoes/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

# --- UTILITIES ---
def search(request):
    q = request.GET.get('q')
    results = Shoe.objects.filter(name__icontains=q) if q else []
    return render(request, 'shoes/search.html', {'results': results, 'query': q})

def wishlist(request):
    return render(request, 'shoes/wishlist.html')

def about(request):
    return render(request, 'shoes/about.html')

def contact(request):
    return render(request, 'shoes/contact.html')

def faq(request):
    return render(request, 'shoes/faq.html')