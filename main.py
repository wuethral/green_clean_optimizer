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

    if hsv_img[y, x][0] > 40 and hsv_img[y, x][0] < 90 and hsv_img[y, x][1] > 90 and hsv_img[y, x][1] < 255 and hsv_img[y, x][2] > 80 and hsv_img[y, x][2] < 255:  # checking, if pixel is green
        return True

def check_pixel_pink(pix, x, y):

    if pix[x, y][0] == 250 and pix[x, y][1] == 14 and pix[x, y][2] == 191:
        return True

def check_pixel_yellow(pix, x, y):

    if pix[x, y][0] == 250 and pix[x, y][1] == 14 and pix[x, y][2] == 190:
        return True


def count_green_pixels_on_edge(pix, x, height, hsv_img):
    add_green = 0
    add_non_green = 0
    for y in range(20, height - 20):
        if not check_pixel_pink(pix, x, y):
            if check_pixel_pink(pix, x, y + 1):
                if check_pixel_green(hsv_img, x, y):
                    add_green += 1
                else:
                    add_non_green += 1
            elif check_pixel_pink(pix, x, y - 1):
                if check_pixel_green(hsv_img, x, y):
                    add_green += 1
                else:
                    add_non_green += 1
            elif check_pixel_pink(pix, x - 1, y):
                if check_pixel_green(hsv_img, x, y):
                    add_green += 1
                else:
                    add_non_green += 1
            elif check_pixel_pink(pix, x + 1, y):
                if check_pixel_green(hsv_img, x, y):
                    add_green += 1
                else:
                    add_non_green += 1
        else:
            add_green += 0
            add_non_green += 0
    return add_green, add_non_green


def errosion_one_pixel(pix, x, height, hsv_img):

    for y in range(20, height-20):
        #if not check_pixel_pink(, x, y):
        if check_pixel_green(hsv_img, x, y):
            if check_pixel_pink(pix, x, y+1):
                pix[x, y] = (250, 14, 190)
            if check_pixel_pink(pix, x, y-1):
                pix[x, y] = (250, 14, 190)
            if check_pixel_pink(pix, x-1, y):
                pix[x, y] = (250, 14, 190)
            if check_pixel_pink(pix, x+1, y):
                pix[x, y] = (250, 14, 190)

''' 
def errosion_second_pixel(pix, x, height):


    for y in range(20, height-20):
        if not check_pixel_pink(pix, x, y) and not check_pixel_yellow(pix, x, y):
            if check_pixel_yellow(pix, x, y+1):
                pix[x, y] = (250, 14, 191)
            if check_pixel_yellow(pix, x, y-1):
                pix[x, y] = (250, 14, 191)
            if check_pixel_yellow(pix, x-1, y):
                pix[x, y] = (250, 14, 191)
            if check_pixel_yellow(pix, x+1, y):
                pix[x, y] = (250, 14, 191)
'''

def turning_yellow_pixels_pink(pix, x, height):

    for y in range(20, height - 20):
        if check_pixel_yellow(pix, x, y):
            pix[x,y] = (250, 14, 191)

def adjust_mask_pixels(pix, mask_pixel, w, h):
    for x_cord in range(w):
        for y_cord in range(h):
            if mask_pixel[x_cord, y_cord] != 0 and check_pixel_pink(pix, x_cord, y_cord):
                mask_pixel[x_cord, y_cord] = 0

def check_black(pix, x, y):
    if pix[x, y][0] == 0 and pix[x, y][1] == 0 and pix[x,y][2] == 0:
        return True

def turn_pink(pix, x, y):
    pix[x, y] = (250, 14, 191)

def turn_black(pix, x, y):
    pix[x, y] = (0, 0, 0)



images = os.listdir('masks_no_errosion_abstract')
masks = os.listdir('PedMasks2')


for i in range(len(images)):
    file_name = images[i]
    mask_name = masks[i]
    #if file_name.startswith('angle') or file_name.startswith('screwdriver') or file_name.startswith('screw') or file_name.startswith('spire1') or file_name.startswith('spire2') or file_name.startswith('zz_test_angle') or file_name.startswith('zz_test_screwdriver') or file_name.startswith('zz_test_screw') or file_name.startswith('zz_test_spire1') or file_name.startswith('zz_test_spire2'):
    #    iterations = 3
    #elif file_name.startswith('hand') or file_name.startswith('zz_test_hand'):
    #    iterations = 2
    #elif file_name.startswith('pliers') or file_name.startswith('zz_test_pliers'):
    #    iterations = 1
    iteration_stopper = False
    first_iteration = True
    clean_counter = 0

    while iteration_stopper == False:
        green_counter = 0
        non_green_counter = 0
        save_name = 'cleaned_images3/' + file_name[:-4] + '_cleaned.png'
        if first_iteration == True:
            print(file_name)
            directory = 'uncleaned_green/' + file_name
            first_iteration = False
        else:
            directory = save_name

        img = Image.open(directory)
        image = cv.imread(directory)
        hsv_img = cv.cvtColor(image, cv.COLOR_BGR2HSV)
        pix = img.load()

        width, height = img.size

        for x in range(30):
            for y in range(30):
                turn_black(pix, x, y)


        for x in range(width):
            for y in range(height):
                if check_black(pix, x, y):
                    turn_pink(pix, x, y)

        for j in range(1):

            for x in range(20, width - 20):

                green, no_green = count_green_pixels_on_edge(pix, x, height, hsv_img)
                green_counter += green
                non_green_counter += no_green
            #print('iteration:', i)
            #print('green_pixels:', green_counter)
            #print('non_green_pixels:', non_green_counter)
            '''
            file = open('infofile3.txt','a')
            text = file_name + ' ' + 'iterations: ' + str(clean_counter) + ' green_pixels: ' + str(green_counter) + ' non_green_pixels: ' + str(non_green_counter) +'\n'
            file.write(text)
            '''
            if non_green_counter != 0:
                ratio_green_nongreen = green_counter/non_green_counter
            else:
                ratio_green_nongreen = 1


            if ratio_green_nongreen >= 0.0001:  #0.3:
                clean_counter += 1

                for x in range(20, width-20):

                    #checking_pixel_value(pix, x, hsv_img, height)
                    errosion_one_pixel(pix, x, height, hsv_img)
                #for x in range(20, width-20):
                    #errosion_second_pixel(pix, x, height)
                for x in range(20, width-20):
                    turning_yellow_pixels_pink(pix, x, height)
            else:

                #text_file = open("cleancounter3.txt", "a")
                #name_for_cleancounterfile = file_name + ': ' + str(clean_counter)
                #text_file.write(name_for_cleancounterfile)
                #text_file.write('\n')
                #text_file.close()
                clean_counter = 0
                mask_directory = 'PedMasks2/' + mask_name
                mask_img = Image.open(mask_directory)
                mask_pixel = mask_img.load()
                adjust_mask_pixels(pix, mask_pixel, width, height)
                iteration_stopper = True
                first_iteration = True


        img.save(save_name)
    mask_save_name = 'new_cleaned_masks_change_pinK_here/' + file_name[:-4] + '_cleaned_mask.png'
    mask_img.save(mask_save_name)
    #file.write('\n')