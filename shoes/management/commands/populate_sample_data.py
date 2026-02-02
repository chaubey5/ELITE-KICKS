from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from shoes.models import Brand, Category, Shoe, Size, Color, ShoeSize, ShoeColor
from decimal import Decimal

class Command(BaseCommand):
    help = 'Populate the database with sample shoe data'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')
        
        # Create brands
        brands_data = [
            {'name': 'Nike', 'description': 'Just Do It'},
            {'name': 'Adidas', 'description': 'Impossible Is Nothing'},
            {'name': 'Puma', 'description': 'Forever Faster'},
            {'name': 'New Balance', 'description': 'Fearlessly Independent'},
            {'name': 'Converse', 'description': 'Made By You'},
        ]
        
        brands = {}
        for brand_data in brands_data:
            brand, created = Brand.objects.get_or_create(
                name=brand_data['name'],
                defaults={'description': brand_data['description']}
            )
            brands[brand.name] = brand
            if created:
                self.stdout.write(f'Created brand: {brand.name}')
        
        # Create categories
        categories_data = [
            {'name': 'Running'},
            {'name': 'Basketball'},
            {'name': 'Casual'},
            {'name': 'Athletic'},
            {'name': 'Formal'},
        ]
        
        categories = {}
        for category_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=category_data['name']
            )
            categories[category.name] = category
            if created:
                self.stdout.write(f'Created category: {category.name}')
        
        # Create sizes
        sizes_data = [7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12]
        sizes = {}
        for size_value in sizes_data:
            size, created = Size.objects.get_or_create(size_value=size_value)
            sizes[size_value] = size
            if created:
                self.stdout.write(f'Created size: {size_value}')
        
        # Create colors
        colors_data = [
            {'name': 'Black', 'hex_code': '#000000'},
            {'name': 'White', 'hex_code': '#FFFFFF'},
            {'name': 'Red', 'hex_code': '#FF0000'},
            {'name': 'Blue', 'hex_code': '#0000FF'},
            {'name': 'Green', 'hex_code': '#008000'},
            {'name': 'Gray', 'hex_code': '#808080'},
        ]
        
        colors = {}
        for color_data in colors_data:
            color, created = Color.objects.get_or_create(
                name=color_data['name'],
                defaults={'hex_code': color_data['hex_code']}
            )
            colors[color.name] = color
            if created:
                self.stdout.write(f'Created color: {color.name}')
        
        # Create shoes
        shoes_data = [
            {
                'name': 'Nike Air Max 270',
                'brand': 'Nike',
                'category': 'Running',
                'description': 'The Nike Air Max 270 delivers unrivaled, all-day comfort. The shoe\'s design draws inspiration from Air Max icons, showcasing Nike\'s greatest innovation with its large window and fresh array of colors.',
                'price': Decimal('129.99'),
                'discount_price': Decimal('99.99'),
                'gender': 'M',
                'stock_quantity': 50,
                'sizes': [8, 9, 10, 11],
                'colors': ['Black', 'White', 'Red']
            },
            {
                'name': 'Adidas Ultraboost 22',
                'brand': 'Adidas',
                'category': 'Running',
                'description': 'The adidas Ultraboost 22 running shoes feature a responsive Boost midsole and a Primeknit+ upper that adapts to your foot for a personalized fit.',
                'price': Decimal('179.99'),
                'discount_price': Decimal('149.99'),
                'gender': 'M',
                'stock_quantity': 30,
                'sizes': [8.5, 9.5, 10.5, 11.5],
                'colors': ['Blue', 'Gray', 'White']
            },
            {
                'name': 'Puma RS-X',
                'brand': 'Puma',
                'category': 'Casual',
                'description': 'The PUMA RS-X is a bold, retro-inspired sneaker with a chunky silhouette and vibrant color combinations that make a statement.',
                'price': Decimal('89.99'),
                'discount_price': Decimal('69.99'),
                'gender': 'M',
                'stock_quantity': 40,
                'sizes': [7, 8, 9, 10, 11, 12],
                'colors': ['Red', 'Blue', 'Green']
            },
            {
                'name': 'New Balance 574',
                'brand': 'New Balance',
                'category': 'Casual',
                'description': 'The New Balance 574 is a classic lifestyle sneaker that combines comfort and style with its ENCAP midsole technology.',
                'price': Decimal('79.99'),
                'discount_price': None,
                'gender': 'M',
                'stock_quantity': 60,
                'sizes': [7.5, 8.5, 9.5, 10.5, 11.5],
                'colors': ['Gray', 'Black', 'White']
            },
            {
                'name': 'Converse Chuck Taylor All Star',
                'brand': 'Converse',
                'category': 'Casual',
                'description': 'The iconic Chuck Taylor All Star is a timeless classic that has been a staple in casual footwear for decades.',
                'price': Decimal('59.99'),
                'discount_price': Decimal('49.99'),
                'gender': 'M',
                'stock_quantity': 100,
                'sizes': [7, 8, 9, 10, 11, 12],
                'colors': ['Black', 'White', 'Red']
            },
            {
                'name': 'Nike LeBron 19',
                'brand': 'Nike',
                'category': 'Basketball',
                'description': 'The Nike LeBron 19 basketball shoes feature innovative cushioning and lockdown support for elite performance on the court.',
                'price': Decimal('199.99'),
                'discount_price': Decimal('179.99'),
                'gender': 'M',
                'stock_quantity': 25,
                'sizes': [8, 9, 10, 11, 12],
                'colors': ['Black', 'Red', 'Blue']
            },
        ]
        
        for shoe_data in shoes_data:
            shoe, created = Shoe.objects.get_or_create(
                name=shoe_data['name'],
                brand=brands[shoe_data['brand']],
                defaults={
                    'category': categories[shoe_data['category']],
                    'description': shoe_data['description'],
                    'price': shoe_data['price'],
                    'discount_price': shoe_data['discount_price'],
                    'gender': shoe_data['gender'],
                    'stock_quantity': shoe_data['stock_quantity'],
                    'is_available': True,
                }
            )
            
            if created:
                # Add sizes
                for size_value in shoe_data['sizes']:
                    ShoeSize.objects.get_or_create(
                        shoe=shoe,
                        size=sizes[size_value],
                        defaults={'stock': 10}
                    )
                
                # Add colors
                for color_name in shoe_data['colors']:
                    ShoeColor.objects.get_or_create(
                        shoe=shoe,
                        color=colors[color_name]
                    )
                
                self.stdout.write(f'Created shoe: {shoe.name}')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully populated database with sample data!')
        )
