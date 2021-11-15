from PIL import Image
import cv2 as cv
import os
import numpy as np

img = Image.open('backgrounded/anglepink1.png')
print(np.array(img)[4:7, 4:7])