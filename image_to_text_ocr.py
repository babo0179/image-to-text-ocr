import pytesseract
from PIL import Image
import os

def extract_text(image_path):
    if not os.path.exists(image_path):
        return "ইমেজ ফাইল পাওয়া যায়নি।"
    
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

if __name__ == "__main__":
    image_path = input("ইমেজ ফাইলের path দিন (JPG/PNG): ")
    text = extract_text(image_path)
    print("\n📄 Extracted Text:")
    print(text)
