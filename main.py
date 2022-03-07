import os
from methods_grean_clean import clean_green_edges


if __name__ == '__main__':

    # Getting the directory the images and corresponding masks we want to clean
    images = os.listdir('images_pink_background')
    masks = os.listdir('masks')

    # Looping through all images
    for i in range(len(images)):
        # Getting file names of image and mask at position i in the corresponding folders
        file_name = images[i]
        mask_name = masks[i]

        # Initializing a boolean iteration stopper as False and a boolean first_iteration to True
        iteration_stopper = False
        first_iteration = True
        # Setting variable clean_counter to 0. Clean counter counts, how many green edges around the object have been
        # cleaned
        clean_counter = 0

        # While the iteration_stopper is False, keep on cleaning green edges (method clean_green_edges)
        while iteration_stopper == False:

            # Calling method clean_green_edges, as long as interation_stopper is False
            iteration_stopper, first_iteration = clean_green_edges(first_iteration, iteration_stopper, file_name,
                                                                                                      mask_name)
