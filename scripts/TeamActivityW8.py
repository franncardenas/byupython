import math
#1 : Ask the user for the number of rows and columns 
#    (note: you are only asking for a single number that will be used for both the rows and the columns).
#1.1 : Display the numbers 1 up to and including that number, each on their own line at this point.

number = int(input("How many columns and rows do you want in your multiplication table?: "))
digit = int(math.log10(number * number)) + 1

for number_rows in range(1, number + 1):
    print('')
    for number_columns in range(1, number + 1):
        number_multiplication = number_rows * number_columns
        print(f'{number_multiplication:{digit}}', end=' ')
        
print()
#2 : Change the program so that the numbers are printed on the same line with a space between them.