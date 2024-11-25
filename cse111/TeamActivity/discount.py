from datetime import datetime
'''
Work as a team to write a Python program named discount.py that gets a customer’s subtotal as 
input and gets the current day of the week from your computer’s operating system. Your program 
must not ask the user to enter the day of the week. Instead, it must get the day of the week from 
your computer’s operating system.

If the subtotal is $50 or greater and today is Tuesday or Wednesday, your program must subtract 10% 
from the subtotal. Your program must then compute the total amount due by adding sales tax of 6% to 
the subtotal. Your program must print the discount amount if applicable, the sales tax amount, and 
the total amount due.

'''
DISC_RATE = 0.10
SALES_TAX_RATE = 0.06

subtotal = 0

print("Enter the price and quantity for each item.")
price = 1
while price != 0:
    # Get the price from the user.
    price = float(input("Please enter the price: "))
    if price != 0:
        # Get the quantity from the user.
        quantity = int(input("Please enter the quantity: "))

        subtotal += price * quantity

        # Print a blank line.
        print()


subtotal = round(subtotal, 2)
print(f"Subtotal: {subtotal:.2f}")
print()

current_date_and_time = datetime.now()

weekday = current_date_and_time.weekday()

if weekday == 1 or weekday == 2:
    if subtotal < 50:
        lacking = 50 - subtotal
        print("To receive the discount, add"
                f" {lacking:.2f} to your order.")
    else:
        discount = round(subtotal * DISC_RATE, 2)
        print(f"Discount amount: {discount:.2f}")
        subtotal -= discount


sales_tax = round(subtotal * SALES_TAX_RATE, 2)
print(f"Sales tax amount: {sales_tax:.2f}")

total = subtotal + sales_tax

print(f"Total: {total:.2f}")
