import PIL
import os
from PIL import Image

path = r'#' #add path to images in quotes ex: 'C:\Users\local\OneDrive\Desktop\images\bag'

for file in os.listdir(path):
    f_img = path + "/" + file
    img = Image.open(f_img)
    img= img.resize( (28,28))
    img.save(f_img)