
from PIL import Image
img =Image.open (‘Beispiel.jpg’)
text = pytesseract.image_to_string(img, config=’’)
print (text)
