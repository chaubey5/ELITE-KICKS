from django.contrib import admin
from .models import (
    Brand, Category, Shoe, ShoeImage, Size, Color,
    ShoeSize, ShoeColor, Cart, CartItem,
    Order, OrderItem, Review, Wishlist,
    ChatSession, ChatMessage
)


# Inline for OrderItem in OrderAdmin
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('total_price',)


# OrderAdmin
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_number',
        'full_name',    # Property in Order model
        'email',
        'total_amount',
        'status',
        'created_at'
    )
    list_filter = ('status', 'payment_method')
    search_fields = ('order_number', 'email')
    inlines = [OrderItemInline]


# OrderItemAdmin
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'shoe',
        'quantity',
        'price',
        'total_price'   # Property in OrderItem model
    )
    readonly_fields = ('total_price',)


# BrandAdmin
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)


# CategoryAdmin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# ShoeAdmin
class ShoeImageInline(admin.TabularInline):
    model = Shoe.additional_images.through
    extra = 1


@admin.register(Shoe)
class ShoeAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'price', 'is_available')
    list_filter = ('brand', 'category', 'gender')
    search_fields = ('name',)
    inlines = [ShoeImageInline]


# SizeAdmin
@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('size_value',)


# ColorAdmin
@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'hex_code')


# ReviewAdmin
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('shoe', 'user', 'rating', 'created_at')
    list_filter = ('rating',)


# WishlistAdmin
@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'shoe', 'created_at')


# CartAdmin (optional, useful for debugging)
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'session_key', 'created_at', 'updated_at')


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'shoe', 'quantity', 'total_price')
    readonly_fields = ('total_price',)


# ChatSessionAdmin
@admin.register(ChatSession)
class ChatSessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'session_key', 'is_active', 'updated_at')


# ChatMessageAdmin
@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('session', 'message_type', 'created_at')
