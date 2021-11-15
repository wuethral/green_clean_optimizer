
def creating_angle_plot():
    x = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    plt.title('bbox')
    plt.xlabel('epoch')
    plt.ylabel(letter)
    plt.plot(x, bbox_values, 'o')
    save_name = 'Bbox_figures/' + letter
    plt.savefig(save_name)



def create_hsv_plot(*args):
    for pos in range(len(args)):
        print(args[pos])
        if args[0] == 'angle_image_1':
            for i in range(1, len(pos)):
                print(args[i])
                #creating_angle_plot(i, args):
        if args[0] == 'hand_image_1':
            for i in range(1, len(pos)):
                print(args[i])
                #creating_angle_plot():
        if args[0] == 'pliers_image_1':
            for i in range(1, len(pos)):
                print(args[i])
                #creating_angle_plot():
        if args[0] == 'screw_image_1':
            for i in range(1, len(pos)):
                print(args[i])
                #creating_angle_plot():
        if args[0] == 'screwdriver_image_1':
            for i in range(1, len(pos)):
                print(args[i])
        if args[0] == 'spire1_image_1':
            for i in range(1, len(pos)):
                print(args[i])
        if args[0] == 'spire2_image_1':
            for i in range(1, len(pos)):
                print(args[i])
        '''

with open("pixel_samples.txt", "r") as a_file:
  for line in a_file:
    stripped_line = line.strip()
    stripped_line = stripped_line.split(':')
    #print(stripped_line)
    if stripped_line[0] == 'angle_image_1':
        if stripped_line[1] == 'green':
            green_values = stripped_line[2].split(',')
            green_values.append('green')
        elif stripped_line[1] == 'blue':
            blue_values = stripped_line[2].split(',')
            blue_values.append('blue')
        elif stripped_line[1] == 'silver':
            silver_values = stripped_line[2].split(',')
            silver_values.append('silver')
        elif stripped_line[1] == 'cord':
            cord_values = stripped_line[2].split(',')
            cord_values.append('cord')
            create_hsv_plot(stripped_line[0], green_values, blue_values, silver_values, cord_values)
    elif stripped_line[0] == 'hand_image_1':
        if stripped_line[1] == 'hand':
            hand_values = stripped_line[2].split(',')
            hand_values.append('hand')
        elif stripped_line[1] == 'green':
            green_values = stripped_line[2].split(',')
            green_values.append('green')
            create_hsv_plot(stripped_line[0], green_values, hand_values)

    elif stripped_line[0] == 'pliers_image_1':
        if stripped_line[1] == 'green':
            green_values = stripped_line[2].split(',')
            green_values.append('green')
        elif stripped_line[1] == 'silver':
            silver_values = stripped_line[2].split(',')
            silver_values.append('silver')
        elif stripped_line[1] == 'cord':
            cord_values = stripped_line[2].split(',')
            cord_values.append('cord')
            create_hsv_plot(stripped_line[0], green_values, silver_values, cord_values)
    elif stripped_line[0] == 'screw_image_1':
        if stripped_line[1] == 'green':
            green_values = stripped_line[2].split(',')
            green_values.append('green')
        elif stripped_line[1] == 'screw_metal':
            screw_metal_values = stripped_line[2].split(',')
            screw_metal_values.append('screw_metal')
        elif stripped_line[1] == 'screw_kunststoff':
            aluminium_values = stripped_line[2].split(',')
            aluminium_values.append('aluminium')
        elif stripped_line[1] == 'cord':
            cord_values = stripped_line[2].split(',')
            cord_values.append('cord')
            create_hsv_plot(stripped_line[0], green_values, screw_metal_values, aluminium_values, cord_values)
    elif stripped_line[0] == 'screwdriver_image_1':
        if stripped_line[1] == 'green':
            green_values = stripped_line[2].split(',')
            green_values.append('green')
        elif stripped_line[1] == 'green_table_wall_interface':
            green_table_wall_interface_values = stripped_line[2].split(',')
            green_table_wall_interface_values.append('green_table_wall')
        elif stripped_line[1] == 'blue':
            blue_values = stripped_line[2].split(',')
            blue_values.append('blue')
        elif stripped_line[1] == 'silver':
            silver_values = stripped_line[2].split(',')
            silver_values.append('silver')
            create_hsv_plot(stripped_line[0], green_values, blue_values, silver_values, green_table_wall_interface_values)
    elif stripped_line[0] == 'spire1_image_1':
        if stripped_line[1] == 'green':
            green_values = stripped_line[2].split(',')
            green_values.append('green')
        elif stripped_line[1] == 'blue':
            blue_values = stripped_line[2].split(',')
            blue_values.append('blue')
        elif stripped_line[1] == 'silver':
            silver_values = stripped_line[2].split(',')
            silver_values.append('silver')
        elif stripped_line[1] == 'cord':
            cord_values = stripped_line[2].split(',')
            cord_values.append('cord')
            create_hsv_plot(stripped_line[0], green_values, blue_values, silver_values, cord_values)
    elif stripped_line[0] == 'spire2_image_1':
        if stripped_line[1] == 'green':
            green_values = stripped_line[2].split(',')
            green_values.append('green')
        elif stripped_line[1] == 'green_table_wall_interface':
            green_table_wall_interface_values = stripped_line[2].split(',')
            green_table_wall_interface_values.append('green_table_wall')
        elif stripped_line[1] == 'blue':
            blue_values = stripped_line[2].split(',')
            blue_values.append('blue')
        elif stripped_line[1] == 'silver':
            silver_values = stripped_line[2].split(',')
            silver_values.append('silver')
        elif stripped_line[1] == 'cord':
            cord_values = stripped_line[2].split(',')
            cord_values.append('cord')
            create_hsv_plot(stripped_line[0], green_values, blue_values, silver_values, cord_values, green_table_wall_interface_values)

