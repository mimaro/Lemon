import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'/home/pi/.local/bin/tesseract'
from PIL import Image
img =Image.open ('Beispiel2.png')
text = pytesseract.image_to_string(img, config='')
print (text)
