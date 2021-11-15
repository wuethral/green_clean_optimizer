from tkinter import *
from PIL import Image, ImageTk
import os
import cv2 as cv



def get_pixel_value(event):
    coordinates = event.x, event.y
    print(hsv_img[coordinates[1]][coordinates[0]])
    print(pixel[coordinates[0], coordinates[1]])


    text_file = open("pixel_samples.txt", "a")
    pixel_value = str(hsv_img[coordinates[1]][coordinates[0]]) + ', '
    text_file.write(pixel_value)
    text_file.close()




#path = 'masks_no_errosion_abstract/pliers_random_dataset_29_2.png'
path = 'trouble_images_cf/zzzz2.png'
#im_name = path.split('/')[1]
#print(im_name)
picture = Image.open(path)
width, height = picture.size
h = int(height/4*3)*7 #int(picture.height/5)
w = int(width/4*3)*7 #int(picture.width/5)
picture = picture.resize((w,h))
image = cv.imread(path)
resized_image = cv.resize(image, (int(w), int(h)))
hsv_img = cv.cvtColor(resized_image, cv.COLOR_BGR2HSV)
pixel = picture.load()





if __name__ == '__main__':
    root = Tk()
    img = ImageTk.PhotoImage(picture.resize((w, h)))

    canvas = Canvas(root, width=int(w), height=int(h))
    canvas.grid(column=0, row=0)
    canvas.create_image(0, 0, anchor=NW, image=img)
    root.bind("<ButtonPress-1>", get_pixel_value)

    mainloop()

