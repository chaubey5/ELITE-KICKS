from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
import requests
from shoes.models import Shoe

class Command(BaseCommand):
    help = 'Update existing shoes with images'

    def handle(self, *args, **options):
        # Shoe images mapping
        shoe_images = {
            'Nike Air Max 270': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500&h=500&fit=crop',
            'Adidas Ultraboost 22': 'https://images.unsplash.com/photo-1608231387042-66d1773070a5?w=500&h=500&fit=crop',
            'Converse Chuck Taylor All Star': 'https://images.unsplash.com/photo-1607522370275-f14206abe5d3?w=500&h=500&fit=crop',
            'Vans Old Skool': 'https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?w=500&h=500&fit=crop',
            'New Balance 990v5': 'https://images.unsplash.com/photo-1556906781-9a412961c28c?w=500&h=500&fit=crop',
            'Puma RS-X': 'https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?w=500&h=500&fit=crop',
            'Reebok Classic Leather': 'https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?w=500&h=500&fit=crop',
            'ASICS Gel-Kayano 28': 'https://images.unsplash.com/photo-1552346154-21d32810aba3?w=500&h=500&fit=crop',
            'Jordan Air 1 Retro High': 'https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=500&h=500&fit=crop',
            'Brooks Ghost 14': 'https://images.unsplash.com/photo-1608231387042-66d1773070a5?w=500&h=500&fit=crop',
            'Saucony Ride 15': 'https://images.unsplash.com/photo-1552346154-21d32810aba3?w=500&h=500&fit=crop',
            'Hoka Clifton 8': 'https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?w=500&h=500&fit=crop',
        }

        updated_count = 0
        for shoe_name, image_url in shoe_images.items():
            try:
                shoe = Shoe.objects.get(name=shoe_name)
                
                # Check if shoe already has an image
                if shoe.image:
                    self.stdout.write(f'Shoe {shoe_name} already has an image, skipping...')
                    continue
                
                # Download and save image
                response = requests.get(image_url)
                if response.status_code == 200:
                    filename = f"{shoe_name.replace(' ', '_').lower()}.jpg"
                    shoe.image.save(filename, ContentFile(response.content), save=True)
                    self.stdout.write(f'Updated image for: {shoe_name}')
                    updated_count += 1
                else:
                    self.stdout.write(f'Failed to download image for: {shoe_name}')
                    
            except Shoe.DoesNotExist:
                self.stdout.write(f'Shoe not found: {shoe_name}')
            except Exception as e:
                self.stdout.write(f'Error updating {shoe_name}: {str(e)}')

        self.stdout.write(self.style.SUCCESS(f'Successfully updated {updated_count} shoes with images!'))







