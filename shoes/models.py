from django.db import models
from django.contrib.auth.models import User

# 1. Basics
class Brand(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Categories"
    def __str__(self): return self.name

class Size(models.Model):
    size_value = models.CharField(max_length=10)
    def __str__(self): return self.size_value

class Color(models.Model):
    name = models.CharField(max_length=50)
    hex_code = models.CharField(max_length=7)
    def __str__(self): return self.name

class ShoeImage(models.Model):
    image = models.ImageField(upload_to='shoes/extra/')
    def __str__(self): return f"Image {self.id}"

# 2. Shoe Core
class Shoe(models.Model):
    GENDER_CHOICES = [('Men', 'Men'), ('Women', 'Women'), ('Unisex', 'Unisex')]
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='shoes/')
    additional_images = models.ManyToManyField(ShoeImage, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    is_available = models.BooleanField(default=True)
    description = models.TextField()

    def __str__(self): return self.name

# 3. Intermediate Models
class ShoeSize(models.Model):
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    def __str__(self): return f"{self.shoe.name} - {self.size.size_value}"

class ShoeColor(models.Model):
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    def __str__(self): return f"{self.shoe.name} - {self.color.name}"

# 4. Cart & Order System
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Cart ka total nikalne ke liye method
    def get_cart_total(self):
        return sum(item.get_total_item_price() for item in self.cartitem_set.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    # YE MISSING THA: Size store karne ke liye field
    size = models.CharField(max_length=10, null=True, blank=True) 
    quantity = models.PositiveIntegerField(default=1)

    def get_total_item_price(self):
        return self.quantity * self.shoe.price
    
    @property
    def total_price(self): 
        return self.get_total_item_price()

    # VIEW KI ERROR FIX: Iska naam exactly wahi rakha jo view dhoond raha hai
    def get_total_item_price(self):
        return self.quantity * self.shoe.price
    
    @property
    def total_price(self): 
        return self.get_total_item_price()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    status = models.CharField(max_length=20, default='Pending')
    payment_method = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    @property
    def full_name(self): return f"{self.user.first_name} {self.user.last_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def get_total_item_price(self):
        return self.quantity * self.price

# 5. Reviews, Wishlist & Chat
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('user', 'shoe') # Duplicate rokne ke liye