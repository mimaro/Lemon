import pytesseract
from PIL import Image
img =Image.open ("Beispiel2.png")
text = pytesseract.image_to_string(img, config="")
print (text)
