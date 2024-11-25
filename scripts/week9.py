
print('Welcome to the Shopping Cart Program!')

items = []
prices = []
menu = ""

while menu != 5:
    print()
    menu = int(input('''Please select one of the following: 
1. Add item 
2. View cart 
3. Remove item 
4. Compute total 
5. Quit 
Please enter an action: '''))


    #ADD A NEW ITEM
    if menu == 1:
        name_item = input('What item would you like to add?: ')
        items.append(name_item)
        price = int(input(f"What is the price of {name_item}?: "))
        prices.append(price)
        print(f'{name_item} has been added to the cart.') 
        print()   


    #DISPLAY THE CONTENTS OF THE SHOPPING CART    
    elif menu == 2:
           print()
           print('The contents of the shopping cart are: ')
           for i in range(len(items)):
            item = items[i]
            price = prices[i]
            print(f"{i+1}. {item} - ${price:.2f}") 
            

    #REMOVE AN ITEM
    elif menu == 3:
           for i in range(len(items)):
            item = items[i]
            price = prices[i]
            print(f"{i+1}. {item} - ${price:.2f}")
            limit = len(items)      
           remove_item = int(input("Please enter the # to remove?: "))
           if remove_item <= limit and remove_item != 0:
             remove_item = remove_item - 1
             items.pop(remove_item) 
             prices.pop(remove_item)
             print('Item removed.')
           else:
               print("Invalid selection") 

    #COMPUTE THE TOTAL
    elif menu == 4:
        total_price = 0
        for price in prices:
            total_price += price 
        print(f'The total price of the items in the shopping cart is ${total_price}')
        
    elif menu == 5:
        print("Thank you. Goodbye.")

        

            
            
        


    














 




#