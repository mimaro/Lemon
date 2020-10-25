import pytesseract
import cv2
from PIL import Image

img =cv2.imread('Gaszaehler.jpg', cv2.IMREAD_COLOR)

gray = cv2.cvtColot(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)

test = pytesseract.image_to_string(gray, config='--oem 3 --psm 12')
print (test)
