from PIL import Image
import cv2 as cv
import os
''' 
def checking_pixel_value(pix, x, hsv_img, height):

    for y in range(20, height - 20):
        if (pix[x, y][0] == 0 and pix[x, y][1] == 0 and pix[x, y][2] == 0) and (pix[x+1, y+1][0] == 0 and pix[x+1, y+1][1] == 0 and pix[x+1, y+1][2] == 0): #or (pix[x, y][0] == 255 and pix[x, y][1] == 192 and pix[x, y][2] == 203):
            if hsv_img[y+1,x][0] > 45 and hsv_img[y+1,x][0] < 90 and hsv_img[y+1,x][1] > 120 and hsv_img[y+1,x][1] < 255 and hsv_img[y+1,x][2] > 0 and hsv_img[y+1,x][2] < 255:
                pix[x, y+1] =(0,0,0)
                break
            if hsv_img[y-1,x][0] > 45 and hsv_img[y-1,x][0] < 90 and hsv_img[y-1,x][1] > 120 and hsv_img[y-1,x][1] < 255 and hsv_img[y-1,x][2] > 0 and hsv_img[y-1,x][2] < 255:
                pix[x, y-1] =(0,0,0)
                break
'''
def check_pixel_green(hsv_img, x, y):

    if hsv_img[y, x][0] > 40 and hsv_img[y, x][0] < 90 and hsv_img[y, x][1] > 100 and hsv_img[y, x][1] < 150 and hsv_img[y, x][2] > 100 and hsv_img[y, x][2] < 255:  # checking, if pixel is green
        return True

def check_pixel_pink(pix, x, y):

    if pix[x, y][0] == 250 and pix[x, y][1] == 14 and pix[x, y][2] == 191:
        return True

def check_pixel_yellow(pix, x, y):

    if pix[x, y][0] == 250 and pix[x, y][1] == 14 and pix[x, y][2] == 190:
        return True

def checking_pixel_value(pix, x, hsv_img, height):

    for y in range(20, height - 20):
        if check_pixel_green(hsv_img, x, y):
            if check_pixel_pink(pix, x, y-1): # checking if pixel above black
                if check_pixel_pink(pix, x+1, y) or check_pixel_pink(pix, x-1, y): #check if left or right pixel black
                    pix[x, y] = (250, 14, 191)
            if check_pixel_pink(pix, x, y+1): # checking if pixel below black
                if check_pixel_pink(pix, x+1, y) or check_pixel_pink(pix, x-1, y): #check if left or right pixel black
                    pix[x, y] = (250, 14, 191)
            if check_pixel_green(hsv_img, x+1, y) and check_pixel_green(hsv_img, x-1, y):
                if check_pixel_pink(pix, x, y-1) and check_pixel_pink(pix, x+1, y-1) and check_pixel_pink(pix, x-1, y-1):
                    pix[x, y] = (250, 14, 191)
                elif check_pixel_pink(pix, x, y+1) and check_pixel_pink(pix, x+1, y+1) and check_pixel_pink(pix, x-1, y+1):
                    pix[x, y] = (250, 14, 191)
            if check_pixel_green(hsv_img, x, y+1) and check_pixel_green(hsv_img, x, y-1):
                if check_pixel_pink(pix, x+1, y-1) and check_pixel_pink(pix, x+1, y) and check_pixel_pink(pix, x+1, y+1):
                    pix[x, y] =(250, 14, 191)
                elif check_pixel_pink(pix, x-1, y-1) and check_pixel_pink(pix, x-1, y) and check_pixel_pink(pix, x-1, y+1):
                    pix[x, y] = (250, 14, 191)



for i in range(30):
    print(i)
    if i == 0:
        directory = 'backgrounded/plierspink29.png'
    else:
        directory = cleaned_save_name
    img = Image.open(directory)
    image = cv.imread(directory)
    hsv_img = cv.cvtColor(image, cv.COLOR_BGR2HSV_FULL)
    pix = img.load()

    width, height = img.size

    for j in range(1):
        for x in range(20, width-20):

            checking_pixel_value(pix, x, hsv_img, height)
    cleaned_save_name = 'cleaned_stuff/cleaned_pliers_' + str(i) +'.png'
    img.save(cleaned_save_name)
