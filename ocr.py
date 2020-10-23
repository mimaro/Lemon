import pytesseract
#pytesseract.pytesseract.tesseract_cmd = r'/home/pi/.local/lib/python3.7/site-packages/pytesseract'
#pytesseract.pytesseract.tesseract_cmd = r'/home/pi/.local/bin/pytesseract'
from PIL import Image
img =Image.open ('Bild.png')
text = pytesseract.image_to_string(img, config='')
print (text)
