from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('shoe/<int:shoe_id>/', views.shoe_detail, name='shoe_detail'),
    path('search/', views.search, name='search'),
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/<int:shoe_id>/', views.add_to_cart, name='add_to_cart'),
    path('update-cart-item/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('remove-cart-item/<int:item_id>/', views.remove_cart_item, name='remove_cart_item'),
    path('clear-cart/', views.clear_cart, name='clear_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
    path('order-history/', views.order_history, name='order_history'),
    path('order-detail/<int:order_id>/', views.order_detail, name='order_detail'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('add-to-wishlist/<int:shoe_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove-from-wishlist/<int:shoe_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('add-review/<int:shoe_id>/', views.add_review, name='add_review'),
    path('quick-rate/<int:shoe_id>/', views.quick_rate, name='quick_rate'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'), # Ye contact page ke liye
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]