import pytesseract
from PIL import Image
from summarizer import summarize_text
import sys

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

if __name__ == "__main__":
    image_path = sys.argv[1]
    text = extract_text_from_image(image_path)
    print("\n[Extracted Text]\n", text)

    summary = summarize_text(text)
    print("\n[Summary]\n", summary)

    with open("outputs/summary.txt", "w") as f:
        f.write(summary)

