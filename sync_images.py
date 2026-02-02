import os
import django

# Django Setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shoe_store.settings')
django.setup()

from shoes.models import Shoe

def sync_shoe_images():
    media_path = os.path.join("media", "shoes")
    
    # Folder ki saari files ki list
    if not os.path.exists(media_path):
        print(f"❌ Error: {media_path} folder nahi mila!")
        return
        
    folder_images = os.listdir(media_path)
    
    # Database ke saare shoes check karein
    shoes = Shoe.objects.all()
    
    print(f"🔍 Scanning {len(shoes)} shoes in database...")
    
    for shoe in shoes:
        # DB mein jo filename hai usse clean karein
        # Example: 'shoes/nike.jpg' -> 'nike.jpg'
        db_filename = os.path.basename(shoe.image.name)
        
        if db_filename in folder_images:
            print(f"✅ OK: {shoe.name} ki photo folder mein hai.")
        else:
            print(f"⚠️ Missing: {shoe.name} ki photo ({db_filename}) folder mein nahi hai!")
            
            # Agar naam milta julta hai toh auto-fix ki koshish (Optional)
            # Yahan hum manually check kar sakte hain ki kya koi similar file hai
            for f in folder_images:
                # Agar shoe name file name mein hai (lowercase check)
                if shoe.name.lower().replace(" ", "_") in f.lower():
                    shoe.image = f"shoes/{f}"
                    shoe.save()
                    print(f"   ✨ Fixed! New path: shoes/{f}")
                    break

if __name__ == "__main__":
    sync_shoe_images()