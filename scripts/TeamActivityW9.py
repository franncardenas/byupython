print('Enter the names and balances of bank accounts (type: quit when done)')
names = []
balances = []
name = None

while name != 'quit':
    name = input('What is the name of this account?')
    if name != 'quit':
        balances.append(float(input('What is the balance? ')))
        names.append(name)
total = 0
highest = 0
a = 0
print('Account Information:')

for i in range(len(names)):
    print(f'{i}. {names[i]} - ${balances[i]}')
    if balances[i] > highest:
        highest = balances[i]
        a = i

for balance in balances:
    total += balance
average = total / len(balances)

print(f'Total: ${total}')
print(f'Average: ${average:.2f}')
print(f'Highest balance: {names[a]} ${balances[a]}')

update = 'yes'

while update == 'yes':
    update = input('Do you want to update an account?')
    if update == 'yes':
        index = int(input('What account index do you want to update?'))
        new_amount = float(input('What is the new amount'))
    balances[index] = new_amount
print('Account Information:')

for i in range(len(names)):
    print(f'{i}. {names[i]} ${balances[i]}')