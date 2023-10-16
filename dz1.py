import math 
from PIL import Image, ImageDraw 
  
w, h = 220, 190
shape = [(40, 40), (w - 10, h - 10)] 
  
# создание объекта Image
img = Image.new("RGB", (w, h)) 
  
# создание линии
img1 = ImageDraw.Draw(img)   
img1.line(shape, fill ="none", width = 0) 
img.show() 