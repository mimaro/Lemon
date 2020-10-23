
from PIL import Image
img =Image.open (Beispiel.png)
text = pytesseract.image_to_string(img, config=’’)
print (text)
