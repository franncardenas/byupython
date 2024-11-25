
#Prompt the user for the age and height of the first person
age = int(input('What is the age of the first rider? '))
height = int(input('What is the height of the first rider? '))

#Then,I ask whether there is a second rider 
second_rider = input('Is there a second rider (yes/no)? ')

if second_rider.lower() == "yes":

    #Ask for their age and height.
    age2 = int(input('What is the age of the second rider? '))
    height2 = int(input('What is the height of the second rider? '))
     
    #No one under 36 inches may ever ride, either by themselves or with another rider. #1
    if height < 36 or height2 < 36:
        print("Sorry, you may not ride.")
    #If there are two riders and one of them is at least 18 years old, they may ride together.#3
    elif age >= 18 or age2 >= 18:
        print("Welcome to the ride. Please be safe and have fun!")
    else: 
        print("Sorry, you may not ride.")

#A single rider can only ride if they are at least 18 years old and are at least 62 inches tall.#2
else :  
    if age >= 18 and height >= 62:
        print("Welcome to the ride. Please be safe and have fun!")
    else:
        print("Sorry, you may not ride.")


