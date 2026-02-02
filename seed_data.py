import os
import django
import random

# Django Setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shoe_store.settings')
django.setup()

from shoes.models import Shoe, Review, Wishlist
from django.contrib.auth.models import User

def seed_remaining_data():
    # 1. User check karein (Review ke liye user chahiye hota hai)
    user = User.objects.first()
    if not user:
        print("❌ Error: Pehle ek superuser banayein (python manage.py createsuperuser)")
        return

    shoes = Shoe.objects.all()
    if not shoes.exists():
        print("❌ Error: Database mein shoes nahi hain. Pehle bulk_add_shoes script chalayein.")
        return

    print("🌱 Seeding data...")

    comments = [
        "Very comfortable and stylish!",
        "Perfect fit, love the color.",
        "Quality is good but delivery was late.",
        "Value for money.",
        "Awesome sneakers, highly recommended!"
    ]

    for shoe in shoes:
        # 2. Fake Reviews add karein
        Review.objects.get_or_create(
            shoe=shoe,
            user=user,
            defaults={
                'rating': random.randint(4, 5),
                'comment': random.choice(comments)
            }
        )

        # 3. Fake Wishlist add karein (Kuch shoes ke liye)
        if random.choice([True, False]):
            Wishlist.objects.get_or_create(user=user, shoe=shoe)

    print("✅ Reviews aur Wishlist items add ho gaye hain!")

if __name__ == "__main__":
    seed_remaining_data()