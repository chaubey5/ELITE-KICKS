# bulk_add_shoes.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shoe_store.settings')
django.setup()

from shoes.models import Brand, Category, Shoe, Size, Color, ShoeSize, ShoeColor

# ------------------ SIZES & COLORS ------------------
sizes_list = ["6", "7", "8", "9", "10", "11"]
colors_list = [
    {"name": "Red", "hex_code": "#FF0000"},
    {"name": "Blue", "hex_code": "#0000FF"},
    {"name": "Black", "hex_code": "#000000"},
    {"name": "White", "hex_code": "#FFFFFF"}
]

for s in sizes_list:
    Size.objects.get_or_create(size_value=s)

for c in colors_list:
    Color.objects.get_or_create(name=c["name"], hex_code=c["hex_code"])

# ------------------ PRODUCTS LIST ------------------
products = [
    {
        "name": "Hoka Clifton 8",
        "brand": "Hoka",
        "category": "Running",
        "description": "Comfortable running shoes",
        "price": 12000.00,
        "discount_price": 9999.00,
        "gender": "M",
        "stock_quantity": 50,
        "sizes": ["8", "9", "10"],
        "colors": ["Red", "Black"],
        "image_name": "ra_hoka_clifton_8.jpg"
    },
    {
        "name": "Nike Air Max 270",
        "brand": "Nike",
        "category": "Sports",
        "description": "Stylish and comfortable",
        "price": 15000.00,
        "discount_price": 13500.00,
        "gender": "U",
        "stock_quantity": 40,
        "sizes": ["7", "8", "9", "10"],
        "colors": ["Blue", "Black"],
        "image_name": "T_nike_air_max_270.jpg"
    },
    {
        "name": "Reebok Classic Leather",
        "brand": "Reebok",
        "category": "Casual",
        "description": "Everyday casual shoes",
        "price": 5000.00,
        "discount_price": None,
        "gender": "U",
        "stock_quantity": 35,
        "sizes": ["6", "7", "8"],
        "colors": ["White", "Black"],
        "image_name": "Ta_reebok_classic_leather.jpg"
    },
    {
        "name": "Vans Old Skool",
        "brand": "Vans",
        "category": "Casual",
        "description": "Classic skate shoes",
        "price": 4500.00,
        "discount_price": 4000.00,
        "gender": "U",
        "stock_quantity": 40,
        "sizes": ["6", "7", "8", "9"],
        "colors": ["Black", "White"],
        "image_name": "ra_vans_old_skool.jpg"
    },
    {
        "name": "Jordan Air 1 Retro High",
        "brand": "Jordan",
        "category": "Sports",
        "description": "Iconic basketball shoes",
        "price": 18000.00,
        "discount_price": 16500.00,
        "gender": "M",
        "stock_quantity": 30,
        "sizes": ["8", "9", "10"],
        "colors": ["Red", "Black"],
        "image_name": "jordan_air_1_retro_high.jpg"
    },
    {
        "name": "New Balance 990v5",
        "brand": "New Balance",
        "category": "Running",
        "description": "Premium running shoes",
        "price": 14000.00,
        "discount_price": 13000.00,
        "gender": "U",
        "stock_quantity": 25,
        "sizes": ["7", "8", "9", "10"],
        "colors": ["White", "Black"],
        "image_name": "new_balance_990v5.jpg"
    },
    {
        "name": "Puma RS-X",
        "brand": "Puma",
        "category": "Casual",
        "description": "Trendy lifestyle sneakers",
        "price": 6000.00,
        "discount_price": 5500.00,
        "gender": "U",
        "stock_quantity": 35,
        "sizes": ["6", "7", "8", "9", "10"],
        "colors": ["Blue", "Black"],
        "image_name": "puma_rs-x.jpg"
    },
    {
        "name": "Saucony Ride 15",
        "brand": "Saucony",
        "category": "Running",
        "description": "Smooth running experience",
        "price": 9000.00,
        "discount_price": 8500.00,
        "gender": "U",
        "stock_quantity": 20,
        "sizes": ["7", "8", "9"],
        "colors": ["Red", "White"],
        "image_name": "saucony_ride_15.jpg"
    }
]

# ------------------ ADDING SHOES ------------------
for p in products:
    brand_obj, _ = Brand.objects.get_or_create(name=p["brand"])
    category_obj, _ = Category.objects.get_or_create(name=p["category"])

    shoe_obj = Shoe.objects.create(
        name=p["name"],
        brand=brand_obj,
        category=category_obj,
        description=p["description"],
        price=p["price"],
        discount_price=p["discount_price"],
        gender=p["gender"],
        stock_quantity=p["stock_quantity"],
        image=f"shoes/{p['image_name']}"  # media/shoes folder ke images
    )

    for size in p["sizes"]:
        size_obj = Size.objects.get(size_value=size)
        ShoeSize.objects.create(shoe=shoe_obj, size=size_obj, stock=p["stock_quantity"])

    for color in p["colors"]:
        color_obj = Color.objects.get(name=color)
        ShoeColor.objects.create(shoe=shoe_obj, color=color_obj, stock=p["stock_quantity"])

print("✅ All shoes added successfully!")
