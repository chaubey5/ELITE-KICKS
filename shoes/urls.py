from django.urls import path
from . import views

urlpatterns = [
    # 1. Main Pages (Shop ka error yahan se theek hoga)
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),  # YAHAN HAI SOLUTION
    path('men/', views.men_collection, name='men_collection'),
    path('shoe/<int:shoe_id>/', views.shoe_detail, name='shoe_detail'),

    # 2. Cart & Checkout (Cart ka error yahan se theek hoga)
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('clear-cart/', views.clear_cart, name='clear_cart'),
    # urls.py mein ye line honi chahiye
    path('order-success/', views.order_confirmation, name='order_confirmation'),
    path('order-confirmation/', views.order_confirmation, name='order_confirmation'),

    # 3. Admin & User Auth
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('add-product/', views.add_product_custom, name='add_product_custom'),

    # 4. Support
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('search/', views.search, name='search'),
    path('remove-item/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update-cart/<int:item_id>/<str:action>/', views.update_cart, name='update_cart'),
    path('add-to-cart/<int:shoe_id>/', views.add_to_cart, name='add_to_cart'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('update-price/<int:shoe_id>/', views.update_price, name='update_price'),
    path('toggle-stock/<int:shoe_id>/', views.toggle_stock, name='toggle_stock'),
    path('delete-product/<int:shoe_id>/', views.delete_product, name='delete_product'),
    path('dashboard/delete/<int:shoe_id>/', views.delete_product, name='delete_product'),
]