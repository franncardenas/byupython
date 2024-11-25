
import math


def compute_area_square(side):
    return compute_area_rectangle(side,side)



def compute_area_rectangle(length, width):
    return length * width




def compute_area_circle(radius):
    return 3.14 * (radius ** 2)

def compute_area(shape, value, value2=0):
    area = -1

    if shape == 'square':
        area = compute_area_square(value)

    elif shape == 'circle':
        area = compute_area_circle(value)

    elif shape == 'rectangle':
        area = compute_area_rectangle(value, value2)

    return area    



shape = ""
while shape != 'quit':
    shape = input('What shape do you want?(square/rectangle/circle): ').lower()

    
    if shape == 'square':
        side = float(input("What is the length of a side of the square? "))
        area = compute_area(shape, side)
        print(area)

    elif shape == 'rectangle':
        #Area of a rectangle
        length = float(input("What is the length of rectangle? "))
        width = float(input("What is the width of the rectangle? "))
        area = compute_area(shape, length, width)
        print(f"The area of the rectangle is: {area}")

    elif shape == 'circle':
        # Area of a circle
        radius = float(input("What is the radius of the circle? "))
        area = compute_area(shape, radius)
        print(f"The area of the circle is: {area}")





    

# # Stretch 1: Using the math library

# radius = float(input("What is the radius of the circle? "))
# area = math.pi * (radius ** 2)
# print(f"The area of the circle is: {area}")

# # Stretch 2: Many areas from one value
# value = float(input("What is the value to be used? "))

# # calculate areas
# area_square = value ** 2
# area_circle = math.pi * (value ** 2)
# volume_cube = value ** 3
# volume_sphere = (4 / 3) * math.pi * (value ** 3)

# # display results
# print(f"Area of a square: {area_square}")
# print(f"Area of a circle: {area_circle}")
# print(f"Volume of a cube: {volume_cube}")
# print(f"Volume of a sphere: {volume_sphere}")



# # Area of a square
# side = float(input("What is the length of a side of the square (in cm)? "))
# area = side ** 2

# print(f"The area of the square is: {area} cm^2")

# # Also, please note that you do NOT put commas in numbers in code (use: 10000, not: 10,000)
# print(f"The area of the square is: {area / 10000} m^2")

# # Area of a rectangle
# length = float(input("What is the length of rectangle (in cm)? "))
# width = float(input("What is the width of the rectangle (in cm)? "))
# area = length * width
# print(f"The area of the rectangle is: {area} cm^2")
# print(f"The area of the rectangle is: {area / 10000} m^2")

# # Area of a circle
# radius = float(input("What is the radius of the circle (in cm)? "))
# area = 3.14 * (radius ** 2)
# print(f"The area of the circle is: {area} cm^2")
# print(f"The area of the circle is: {area / 10000} m^2")

