from PIL import Image
import cv2 as cv


def count_green_pixels_on_edge(pix, x, height, hsv_img):
    '''Method to count how many green and non green pixels on the edge along the 1 x-axis'''

    # Initializing add_green and add_non_green to zero as a variable to count green and non green pixels on edge of obj.
    add_green = 0
    add_non_green = 0

    # Looping through y-axis
    for y in range(20, height - 20):
        # If the pixel is not pink
        if not check_pixel_pink(pix, x, y):
            # and the pixel on the bottom is pink
            if check_pixel_pink(pix, x, y + 1):
                # check if the pixel is green and if yes, add 1 to add_green
                if check_pixel_green(hsv_img, x, y):
                    add_green += 1
                # if no, add 1 to add_non_green
                else:
                    add_non_green += 1
            # and the pixel on the top is pink
            elif check_pixel_pink(pix, x, y - 1):
                # check if the pixel is green and if yes, add 1 to add_green
                if check_pixel_green(hsv_img, x, y):
                    add_green += 1
                # if no, add 1 to add_non_green
                else:
                    add_non_green += 1
            # and the pixel to the left is pink
            elif check_pixel_pink(pix, x - 1, y):
                # check if the pixel is green and if yes, add 1 to add_green
                if check_pixel_green(hsv_img, x, y):
                    add_green += 1
                # if no, add 1 to add_non_green
                else:
                    add_non_green += 1
            # and the pixel to the right is pink
            elif check_pixel_pink(pix, x + 1, y):
                # check if the pixel is green and if yes, add 1 to add_green
                if check_pixel_green(hsv_img, x, y):
                    add_green += 1
                # if no, add 1 to add_non_green
                else:
                    add_non_green += 1
        # Otherwise, do nothing
        else:
            add_green += 0
            add_non_green += 0

    return add_green, add_non_green


def errosion_one_pixel(pix, x, height, hsv_img):
    '''Method to check if pink pixel is next to green pixel and if so, turn it pink'''

    for y in range(20, height - 20):
        # Check, if pixel is green
        if check_pixel_green(hsv_img, x, y):
            # Check, if bottom pixel is pink
            if check_pixel_pink(pix, x, y + 1):
                # Turn pixel pink
                pix[x, y] = (250, 14, 190)
            # Check, if top pixel is pink
            if check_pixel_pink(pix, x, y - 1):
                # Turn pixel pink
                pix[x, y] = (250, 14, 190)
            # Check, if left pixel is pink
            if check_pixel_pink(pix, x - 1, y):
                # Turn pixel pink
                pix[x, y] = (250, 14, 190)
            # Check, if right pixel is pink
            if check_pixel_pink(pix, x + 1, y):
                # Turn pixel pink
                pix[x, y] = (250, 14, 190)


def turning_yellow_pixels_pink(pix, x, height):
    '''Method to turn yellow pixels to black pixels'''

    for y in range(20, height - 20):
        if check_pixel_yellow(pix, x, y):
            pix[x, y] = (250, 14, 191)


def adjust_mask_pixels(pix, mask_pixel, w, h):
    '''Method that turns all mask pixels of the pink image pixels to black'''

    for x_cord in range(w):
        for y_cord in range(h):
            if mask_pixel[x_cord, y_cord] != 0 and check_pixel_pink(pix, x_cord, y_cord):
                mask_pixel[x_cord, y_cord] = 0


def check_black(pix, x, y):
    '''Method to check if a pixel is black'''

    if pix[x, y][0] == 0 and pix[x, y][1] == 0 and pix[x, y][2] == 0:
        return True


def check_pixel_green(hsv_img, x, y):
    '''Method to check, if a pixel is green'''

    if hsv_img[y, x][0] > 40 and hsv_img[y, x][0] < 90 and hsv_img[y, x][1] > 90 and hsv_img[y, x][1] < 255 and \
            hsv_img[y, x][2] > 80 and hsv_img[y, x][2] < 255:  # checking, if pixel is green
        return True


def check_pixel_pink(pix, x, y):
    '''Method to check, if a pixel is pink'''

    if pix[x, y][0] == 250 and pix[x, y][1] == 14 and pix[x, y][2] == 191:
        return True


def check_pixel_yellow(pix, x, y):
    '''Method to check, if a pixel is yellow'''

    if pix[x, y][0] == 250 and pix[x, y][1] == 14 and pix[x, y][2] == 190:
        return True


def turn_pink(pix, x, y):
    '''Method to turn pixel pink'''

    pix[x, y] = (250, 14, 191)


def turn_black(pix, x, y):
    '''Method to turn pixel black'''

    pix[x, y] = (0, 0, 0)


def clean_edges(img, save_name, first_iteration, iteration_stopper, file_name, mask_name, pix, hsv_img, width, height):
    '''Method to clean green edges'''

    # Setting counters to count the green/non-green pixels on the edge of the object
    green_counter = 0
    non_green_counter = 0

    # Looping through all x coordinates of the image
    for x in range(20, width - 20):
        # Counting the green and non green pixels on the edge of object and adding them to a counter
        green, no_green = count_green_pixels_on_edge(pix, x, height, hsv_img)
        green_counter += green
        non_green_counter += no_green

    # After counting all green and non green pixels on the edge, the ration of green and non_green pixels is calcluated
    if non_green_counter != 0:
        ratio_green_nongreen = green_counter / non_green_counter
    else:
        ratio_green_nongreen = 1

    # If the ration of green and non green pixels is larger then a ceratin threshold, the edge pixels are cleaned off
    # (turned to pink for image and black for mask)
    if ratio_green_nongreen >= 0.3:
        for x in range(20, width - 20):
            # checking_pixel_value(pix, x, hsv_img, height)
            errosion_one_pixel(pix, x, height, hsv_img)

        # Turning the yellow pixels form erosion to pink
        for x in range(20, width - 20):
            turning_yellow_pixels_pink(pix, x, height)
        # After one edge of green pixels has been eroded, the image can be save in cleaned images
        img.save(save_name)
    else:
        # When the ratio of green and non green pixels is below the threshold, the cleaning of the image is finished and
        # the masks can be created.

        # Opening and resizing masks
        mask_directory = 'masks/' + mask_name
        mask_img = Image.open(mask_directory)
        mask_img = mask_img.resize((1920, 1080))
        # Loading mask pixels
        mask_pixel = mask_img.load()
        # Method to turn mask pixels of the images pixels, that have been eroded, black
        adjust_mask_pixels(pix, mask_pixel, width, height)

        # Iteration_stopper is set to True, because there is no additional iteration needed
        iteration_stopper = True
        # first_iteration set to True for the next image
        first_iteration = True

        # Saving the mask
        mask_save_name = 'cleaned_masks/' + file_name
        mask_img.save(mask_save_name)

    return first_iteration, iteration_stopper

def clean_green_edges(first_iteration, iteration_stopper, file_name, mask_name):
    '''Mein method to clean green edges'''

    # Path, to images in folder cleaned_images (for accessing and saving)
    save_name = 'cleaned_images/' + file_name
    # When in the first iteration, the original, uncleaned images has to be opened.
    if first_iteration == True:
        directory = 'images_pink_background/' + file_name
        # After the first iteration is executed, the boolean first_iteration is set to False
        first_iteration = False
    else:
        # If it is not the first iteration, the image cleaned in the last iteration should be accessed.
        directory = save_name

    # Opening the images in pillow and open-cv
    img = Image.open(directory)
    image = cv.imread(directory)
    # Turning bgr image to hvs
    hsv_img = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    # Accessing the pixel from img
    pix = img.load()
    # Getting the width and height form img
    width, height = img.size

    # Turning all pixels in the background pink (green screen to pink pixels)
    img.save('bla.png')

    # Method to clean edges
    first_iteration, iteration_stopper = clean_edges(img, save_name, first_iteration, iteration_stopper, file_name,
                                                         mask_name, pix, hsv_img, width, height)


    return first_iteration, iteration_stopper
