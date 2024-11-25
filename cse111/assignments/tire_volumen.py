import math 
from datetime import datetime

#get date 
current_date_and_time = datetime.now()

#Get width, aspect ratio and diameter of the wheel from user.
width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter_wheel = float(input("Enter the diameter of the wheel in inches (ex 15): "))

top_result = math.pi*width**2*aspect_ratio*(width*aspect_ratio+2540*diameter_wheel)

volum = round(top_result / 10000000000, 2)

print(f"The approximate volume is {volum} liters")

buy = input("Do you want to buy tires with the dimensions you entered? (yes/no): ")

if buy.lower() == 'yes': 

    phone = input("Enter your cell phone number: ")

    with open("volumes.txt", "at") as volumes_file:

    # Print a date, volumes and cell phone number to the file.
        print(f"{current_date_and_time:%Y-%m-%d}, {width:.0f}, {aspect_ratio:.0f}, {diameter_wheel:.0f}, {volum}, {phone}", file=volumes_file)
else : 

    # Open a text file named volumes.txt in append mode.
    with open("volumes.txt", "at") as volumes_file:

        # Print a date and volumes to the file.
        print(f"{current_date_and_time:%Y-%m-%d}, {width:.0f}, {aspect_ratio:.0f}, {diameter_wheel:.0f}, {volum}", file=volumes_file)