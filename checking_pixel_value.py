from PIL import Image
import cv2 as cv
import os

img = Image.open('backgrounded/anglepink1.png')
pix = img.load()
print(pix[0,0])
print(pix[1,1])