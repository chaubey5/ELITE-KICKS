from django.contrib import admin
from .models import (
    Brand, Category, Shoe, ShoeImage, Size, Color,
    ShoeSize, ShoeColor, Cart, CartItem,
    Order, OrderItem, Wishlist
)

# --- Inlines (Inventory Management ko easy banane ke liye) ---
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class ShoeSizeInline(admin.TabularInline):
    model = ShoeSize
    extra = 1

class ShoeColorInline(admin.TabularInline):
    model = ShoeColor
    extra = 1

# ManyToMany Inline Fix
class ShoeImageInline(admin.TabularInline):
    model = Shoe.additional_images.through 
    extra = 1

# --- Admin Registrations ---

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'full_name', 'email', 'total_amount', 'status', 'created_at')
    list_filter = ('status', 'payment_method')
    search_fields = ('order_number', 'email', 'user__username')
    inlines = [OrderItemInline]

@admin.register(Shoe)
class ShoeAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'price', 'is_available')
    list_filter = ('brand', 'category', 'gender', 'is_available')
    search_fields = ('name',)
    inlines = [ShoeImageInline, ShoeSizeInline, ShoeColorInline]
    exclude = ('additional_images',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('size_value',)

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'hex_code')

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'shoe', 'quantity', 'get_total_item_price')

# --- Baki Models Registration ---
admin.site.register(Category)
admin.site.register(ShoeImage)
admin.site.register(ShoeSize)
admin.site.register(ShoeColor)
admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(OrderItem)