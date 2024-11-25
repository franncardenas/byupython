# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    
    draw_sky(canvas, scene_width, scene_height) 

    draw_ground(canvas, scene_width, scene_height)
    #draw_grid(canvas, scene_width, scene_height, 50)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height, width=0, fill="sky blue")

    #draw a cloud. 
    x_start_cloud = 600
    y_start_cloud = 400
    draw_cloud(canvas, x_start_cloud, y_start_cloud)

    #draw another cloud
    x_start_cloud = 250
    y_start_cloud = 350
    draw_cloud(canvas, x_start_cloud, y_start_cloud)


    #draw sun
    x_sun = 80
    y_sun = 400
    draw_sun(canvas, x_sun, y_sun)


    #draw birds
    bird_center = 300
    bird_top = 400
    draw_bird(canvas, bird_center, bird_top)

    bird_center = 600
    bird_top = 450
    draw_bird(canvas, bird_center, bird_top)

    bird_center = 500
    bird_top = 420
    draw_bird(canvas, bird_center, bird_top)


def draw_cloud(canvas, x_start_cloud, y_start_cloud):

    x_cloud_left = x_start_cloud - 75
    x_cloud_right = x_start_cloud + 75
    y_end_cloud = y_start_cloud+30
    for x in [1,2,3]:
        draw_oval(canvas, x_cloud_left, y_start_cloud, x_cloud_right, y_end_cloud, width=0, fill="white")
        x_cloud_left += 50
        y_start_cloud += 10
        x_cloud_right += 20
        y_end_cloud += 10
            
    draw_oval(canvas, x_cloud_left-50, y_start_cloud+5, x_cloud_right+30, y_end_cloud-55, width=0, fill="white")


def draw_sun(canvas, x_sun, y_sun):

    diameter = 90
    draw_oval(canvas, x_sun, y_sun,
                    x_sun + diameter, y_sun + diameter, width=0, fill="yellow2")


def draw_bird(canvas, bird_center, bird_top):

    bird_center_2 = bird_center - 100
    bird_center_2x = bird_center + 100
    bird_top2 = bird_top +20
    draw_arc(canvas, bird_center_2, bird_top2, bird_center, bird_top, start=0, extent=60)
    draw_arc(canvas, bird_center, bird_top2, bird_center_2x, bird_top,start=120, extent=70)
    

def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="tan4")

    #draw mountains
    center_x = 650
    bottom = scene_height / 3
    height = 200
    draw_mountain(canvas, center_x, bottom, height)
    center_x = 430
    bottom = scene_height / 3
    height = 200
    draw_mountain(canvas, center_x, bottom, height)
    

    # Draw some pine trees.
    tree_center_x = 20
    tree_bottom = 160
    tree_height = 80
    for i in [1,2,3,4,5,6,7,8,9]:
        draw_pine_tree(canvas, tree_center_x,
                tree_bottom, tree_height)
        tree_center_x+=35
    # Draw another pine tree.
    tree_center_x = 750
    tree_bottom = 90
    tree_height = 180
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

    #draw sun
    x_sun = 400
    y_sun = 50
    draw_lake(canvas, x_sun, y_sun)
    

def draw_pine_tree(canvas, center_x, bottom, height):
    """Draw a single pine tree.
    Parameters
        canvas: The canvas where this function
            will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="dark green")

def draw_mountain(canvas, center_x, bottom, height):

    skirt_width = height / 1.3
    skirt_left = center_x - skirt_width / 1.3
    skirt_right = center_x + skirt_width / 1.3
    skirt_top = bottom + height

    
    for i in [1,2]:
        draw_polygon(canvas, center_x, skirt_top,
                skirt_right, bottom,
                skirt_left, bottom,
                outline="gray57", width=1, fill="gray57")
        center_x+=100
        skirt_top+=40
        skirt_right+=100
        skirt_left+=80

def draw_bird(canvas, bird_center, bird_top):

    bird_center_2 = bird_center - 100
    bird_center_2x = bird_center + 100
    bird_top2 = bird_top +20
    draw_arc(canvas, bird_center_2, bird_top2, bird_center, bird_top, start=0, extent=60)
    draw_arc(canvas, bird_center, bird_top2, bird_center_2x, bird_top,start=120, extent=70)

def draw_lake(canvas, x_sun, y_sun):
    
    diameter = 90
    space = 200
    draw_oval(canvas, x_sun, y_sun,
                    x_sun + space, y_sun + diameter, width=1, fill="tan3")
    draw_oval(canvas, x_sun, y_sun,
                    x_sun + space, y_sun + diameter/1.1, width=1, fill="dodgerBlue1")


def draw_grid(canvas, width, height, interval, color="blue"):
    # Draw a vertical line at every x interval.
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text(canvas, x, label_y, f"{x}", fill=color)

    # Draw a horizontal line at every y interval.
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text(canvas, label_x, y, f"{y}", fill=color)
# Call the main function so that
# this program will start executing.
main()