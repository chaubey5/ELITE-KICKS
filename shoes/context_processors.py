from .models import Cart

def cart_processor(request):
    """Add cart to the template context"""
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        cart = None
        if request.session.session_key:
            try:
                cart = Cart.objects.get(session_key=request.session.session_key)
            except Cart.DoesNotExist:
                pass
    
    return {'cart': cart}







