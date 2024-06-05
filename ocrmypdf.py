
import cv2
import pytesseract
from pytesseract import Output
pytesseract.pytesseract.tesseract_cmd=r'C:\Users\Aren1\AppData\Local\Programs\Tesseract-OCR\tesseract'


img = cv2.imread('invoice-sample.jpg')

d = pytesseract.image_to_string(img, output_type=Output.DICT)
print(d.keys())
