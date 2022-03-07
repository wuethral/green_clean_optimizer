import cv2
import os
import numpy as np


image_name_list = os.listdir('images')

pink_background = cv2.imread('background.png')
pink_background = cv2.resize(pink_background, (1920, 1080))

for image_name in image_name_list:
    print(image_name)
    image_path = 'images/' + image_name
    image = cv2.imread(image_path)
    image=cv2.resize(image,(1920,1080))

    mask_path = 'masks/' + image_name
    mask = cv2.imread(mask_path)
    mask=cv2.resize(mask,(1920,1080))

    new_image = np.where(mask==0, pink_background, image)
    new_image_path = 'images_pink_background/' + image_name
    cv2.imwrite(new_image_path, new_image)