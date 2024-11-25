from PIL import Image

#Type names of images
frontal_image = input("Type the name of the image you want to use as the front image: ")
back_image = input("Type the name of the image you want to use as the back image: ")

#Load green image and background image
image_foreground = Image.open(frontal_image)
image_background = Image.open(back_image)

#image_snow.show()
#image_penguin.show()
image_new = Image.new("RGB", image_background.size)

#(width, height) = image_background.size
#Pixels of images
pixels_foreground = image_foreground.load()
pixels_background = image_background.load()
pixels_new = image_new.load()

for width_x in range(image_foreground.width):
    for height_y in range(image_foreground.height):
        (r , g, b) = pixels_foreground[width_x, height_y]
        if r < 220 and g > 125 and b < 100: 
            pixels_new[width_x, height_y] = pixels_background[width_x, height_y]
        else : 
            pixels_new[width_x, height_y] = pixels_foreground[width_x, height_y]
image_new.show()

#save image
image_new.save("finalimage.jpg")


#width, height = image_snow.size
#print(image_snow.size)
#print(width)
#print(height)


#print(pixels_snow[200, 100])
#print(pixels_snow[201, 100])
#print(pixels_snow[202, 100])
#print(pixels_snow[203, 100])
#print(pixels_snow[204, 100])

#pixels_snow[200, 100] = (0, 0, 255)
#pixels_snow[201, 100] = (0, 0, 255)
#pixels_snow[202, 100] = (0, 0, 255)
#pixels_snow[203, 100] = (0, 0, 255)
#pixels_snow[204, 100] = (0, 0, 255)

