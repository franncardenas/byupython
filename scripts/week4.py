#Ask the user for the price of a child and an adult meal(float values) 
childs_meal = float(input("What is the price of a child's meal?: "))
adult_meal = float(input("What is the price of an adult's meal?: "))

#Ask the user for the number of adults and children(integer values)
children = int(input("How many children are there??: "))
adults = int(input("How many adults are there?: "))

#Ask the user for the sales tax rate(float values)
tax_rate = float(input("What is the sales tax rate?: "))

print('')
#Compute and display the subtotal
sub_total = (childs_meal * children) + (adult_meal * adults)
print(f"Subtotal:   ${sub_total:>6.2f}")

#sales tax
sales_tax = tax_rate/100 * sub_total
print(f"Sales Tax:  ${sales_tax:>6.2f}")

#Compute and display the total
total = sub_total + sales_tax 
print(f"Total:      ${total:>6.2f}")

print('')
#Ask the user for the payment amount
payment = float(input("What is the payment amount?: "))
change = payment - total 
print(f'Change:     ${change:>6.2f}')

print('')
#a dessert
print(f"Would you like to bring a dessert for only 1 dollar extra?: ")
print('No: 0')
print('Si: 1')
answer = int(input('Answer: '))
print('')
total = total + answer
change = change - answer

print(f'Total due:  ${total:>6.2f}')
print(f'Change:     ${change:>6.2f}')
print('')
print('¡Enjoy your meal!')

