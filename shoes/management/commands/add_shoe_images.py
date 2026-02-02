from django.core.management.base import BaseCommand
from django.core.files import File
from django.core.files.base import ContentFile
import requests
import os
from shoes.models import Shoe, Brand, Category, Size, Color, ShoeSize, ShoeColor

class Command(BaseCommand):
    help = 'Add sample shoe images with proper names'

    def handle(self, *args, **options):
        # Sample shoes with images
        shoes_data = [
            {
                'name': 'Nike Air Max 270',
                'brand': 'Nike',
                'category': 'Running',
                'price': 150.00,
                'description': 'The Nike Air Max 270 delivers unrivaled, all-day comfort. The shoe\'s design draws inspiration from Air Max icons, showcasing Nike\'s greatest innovation with its large window and fresh array of colors.',
                'gender': 'U',
                'stock_quantity': 50,
                'image_url': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500&h=500&fit=crop',
                'sizes': ['7', '8', '9', '10', '11', '12'],
                'colors': ['Black', 'White', 'Red']
            },
            {
                'name': 'Adidas Ultraboost 22',
                'brand': 'Adidas',
                'category': 'Running',
                'price': 180.00,
                'description': 'The adidas Ultraboost 22 running shoes feature a responsive Boost midsole and a Primeknit+ upper for a sock-like fit that adapts to your foot.',
                'gender': 'M',
                'stock_quantity': 45,
                'image_url': 'https://images.unsplash.com/photo-1608231387042-66d1773070a5?w=500&h=500&fit=crop',
                'sizes': ['7', '8', '9', '10', '11', '12'],
                'colors': ['Blue', 'Grey', 'Black']
            },
            {
                'name': 'Converse Chuck Taylor All Star',
                'brand': 'Converse',
                'category': 'Casual',
                'price': 65.00,
                'description': 'The iconic Chuck Taylor All Star sneaker features a canvas upper, rubber toe cap, and vulcanized rubber sole for timeless style and comfort.',
                'gender': 'U',
                'stock_quantity': 100,
                'image_url': 'https://images.unsplash.com/photo-1607522370275-f14206abe5d3?w=500&h=500&fit=crop',
                'sizes': ['6', '7', '8', '9', '10', '11', '12'],
                'colors': ['White', 'Black', 'Red', 'Navy']
            },
            {
                'name': 'Vans Old Skool',
                'brand': 'Vans',
                'category': 'Skateboarding',
                'price': 60.00,
                'description': 'The Vans Old Skool features the iconic side stripe, durable canvas upper, and vulcanized waffle outsole for superior board feel and durability.',
                'gender': 'U',
                'stock_quantity': 75,
                'image_url': 'https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?w=500&h=500&fit=crop',
                'sizes': ['6', '7', '8', '9', '10', '11', '12'],
                'colors': ['Black', 'White', 'Grey', 'Blue']
            },
            {
                'name': 'New Balance 990v5',
                'brand': 'New Balance',
                'category': 'Running',
                'price': 185.00,
                'description': 'The New Balance 990v5 features a premium pigskin and mesh upper, ENCAP midsole technology, and a durable rubber outsole for superior comfort and support.',
                'gender': 'M',
                'stock_quantity': 30,
                'image_url': 'https://images.unsplash.com/photo-1556906781-9a412961c28c?w=500&h=500&fit=crop',
                'sizes': ['7', '8', '9', '10', '11', '12'],
                'colors': ['Grey', 'Black', 'Navy']
            },
            {
                'name': 'Puma RS-X',
                'brand': 'Puma',
                'category': 'Lifestyle',
                'price': 110.00,
                'description': 'The Puma RS-X features a chunky retro design with bold colors, a padded collar, and a comfortable midsole for a statement-making look.',
                'gender': 'U',
                'stock_quantity': 40,
                'image_url': 'https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?w=500&h=500&fit=crop',
                'sizes': ['6', '7', '8', '9', '10', '11', '12'],
                'colors': ['White', 'Black', 'Pink', 'Blue']
            },
            {
                'name': 'Reebok Classic Leather',
                'brand': 'Reebok',
                'category': 'Lifestyle',
                'price': 75.00,
                'description': 'The Reebok Classic Leather features a premium leather upper, padded collar, and a durable rubber outsole for timeless style and comfort.',
                'gender': 'U',
                'stock_quantity': 60,
                'image_url': 'https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?w=500&h=500&fit=crop',
                'sizes': ['6', '7', '8', '9', '10', '11', '12'],
                'colors': ['White', 'Black', 'Grey', 'Navy']
            },
            {
                'name': 'ASICS Gel-Kayano 28',
                'brand': 'ASICS',
                'category': 'Running',
                'price': 160.00,
                'description': 'The ASICS Gel-Kayano 28 features GEL technology, FlyteFoam midsole, and a breathable mesh upper for maximum comfort and support during long runs.',
                'gender': 'M',
                'stock_quantity': 35,
                'image_url': 'https://images.unsplash.com/photo-1552346154-21d32810aba3?w=500&h=500&fit=crop',
                'sizes': ['7', '8', '9', '10', '11', '12'],
                'colors': ['Grey', 'Blue', 'Black']
            },
            {
                'name': 'Jordan Air 1 Retro High',
                'brand': 'Nike',
                'category': 'Basketball',
                'price': 170.00,
                'description': 'The Jordan Air 1 Retro High features a premium leather upper, Air-Sole unit in the midsole, and a durable rubber outsole for classic basketball style.',
                'gender': 'U',
                'stock_quantity': 25,
                'image_url': 'https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=500&h=500&fit=crop',
                'sizes': ['7', '8', '9', '10', '11', '12'],
                'colors': ['Red', 'Black', 'White', 'Blue']
            },
            {
                'name': 'Brooks Ghost 14',
                'brand': 'Brooks',
                'category': 'Running',
                'price': 130.00,
                'description': 'The Brooks Ghost 14 features DNA LOFT cushioning, a breathable mesh upper, and a smooth ride for everyday training runs.',
                'gender': 'W',
                'stock_quantity': 40,
                'image_url': 'https://images.unsplash.com/photo-1608231387042-66d1773070a5?w=500&h=500&fit=crop',
                'sizes': ['6', '7', '8', '9', '10', '11'],
                'colors': ['Grey', 'Pink', 'Blue', 'Black']
            },
            {
                'name': 'Saucony Ride 15',
                'brand': 'Saucony',
                'category': 'Running',
                'price': 120.00,
                'description': 'The Saucony Ride 15 features PWRRUN cushioning, a breathable mesh upper, and a smooth ride for neutral runners.',
                'gender': 'M',
                'stock_quantity': 30,
                'image_url': 'https://images.unsplash.com/photo-1552346154-21d32810aba3?w=500&h=500&fit=crop',
                'sizes': ['7', '8', '9', '10', '11', '12'],
                'colors': ['Blue', 'Grey', 'Orange', 'Black']
            },
            {
                'name': 'Hoka Clifton 8',
                'brand': 'Hoka',
                'category': 'Running',
                'price': 130.00,
                'description': 'The Hoka Clifton 8 features a lightweight design, EVA midsole, and a breathable mesh upper for a smooth, cushioned ride.',
                'gender': 'U',
                'stock_quantity': 35,
                'image_url': 'https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?w=500&h=500&fit=crop',
                'sizes': ['6', '7', '8', '9', '10', '11', '12'],
                'colors': ['White', 'Black', 'Blue', 'Grey']
            }
        ]

        # Create or get brands
        brands = {}
        for brand_name in ['Nike', 'Adidas', 'Converse', 'Vans', 'New Balance', 'Puma', 'Reebok', 'ASICS', 'Brooks', 'Saucony', 'Hoka']:
            brand, created = Brand.objects.get_or_create(name=brand_name)
            brands[brand_name] = brand
            if created:
                self.stdout.write(f'Created brand: {brand_name}')

        # Create or get categories
        categories = {}
        for category_name in ['Running', 'Casual', 'Skateboarding', 'Lifestyle', 'Basketball']:
            category, created = Category.objects.get_or_create(name=category_name)
            categories[category_name] = category
            if created:
                self.stdout.write(f'Created category: {category_name}')

        # Create or get sizes
        sizes = {}
        for size_value in ['6', '7', '8', '9', '10', '11', '12']:
            size, created = Size.objects.get_or_create(size_value=size_value)
            sizes[size_value] = size
            if created:
                self.stdout.write(f'Created size: {size_value}')

        # Create or get colors
        colors = {}
        for color_name in ['Black', 'White', 'Red', 'Blue', 'Grey', 'Navy', 'Pink', 'Orange']:
            color, created = Color.objects.get_or_create(name=color_name)
            colors[color_name] = color
            if created:
                self.stdout.write(f'Created color: {color_name}')

        # Create shoes with images
        for shoe_data in shoes_data:
            # Check if shoe already exists
            if Shoe.objects.filter(name=shoe_data['name']).exists():
                self.stdout.write(f'Shoe already exists: {shoe_data["name"]}')
                continue

            # Create shoe
            shoe = Shoe.objects.create(
                name=shoe_data['name'],
                brand=brands[shoe_data['brand']],
                category=categories[shoe_data['category']],
                price=shoe_data['price'],
                description=shoe_data['description'],
                gender=shoe_data['gender'],
                stock_quantity=shoe_data['stock_quantity'],
                is_available=True
            )

            # Download and save image
            try:
                response = requests.get(shoe_data['image_url'])
                if response.status_code == 200:
                    # Save image with proper filename
                    filename = f"{shoe_data['name'].replace(' ', '_').lower()}.jpg"
                    shoe.image.save(filename, ContentFile(response.content), save=True)
                    self.stdout.write(f'Added image for: {shoe_data["name"]}')
                else:
                    self.stdout.write(f'Failed to download image for: {shoe_data["name"]}')
            except Exception as e:
                self.stdout.write(f'Error downloading image for {shoe_data["name"]}: {str(e)}')

            # Add sizes
            for size_value in shoe_data['sizes']:
                ShoeSize.objects.create(
                    shoe=shoe,
                    size=sizes[size_value],
                    stock=10
                )

            # Add colors
            for color_name in shoe_data['colors']:
                ShoeColor.objects.create(
                    shoe=shoe,
                    color=colors[color_name]
                )

            self.stdout.write(f'Created shoe: {shoe_data["name"]}')

        self.stdout.write(self.style.SUCCESS('Successfully added shoes with images!'))
