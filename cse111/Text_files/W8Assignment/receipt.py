from datetime import datetime
import csv 

current_date_and_time = datetime.now()
day = datetime.strftime(datetime.now(), '%A')

def main():
    
    try:
        

        NUMBER_PRODUCT = 0
        products_dict = read_dictionary('Text_files\W8Assignment\products.csv', NUMBER_PRODUCT)
        #print(products_dict)

        filename2 = r"Text_files\W8Assignment\request.csv"
        with open(filename2, "rt") as request_file:
            
            reader = csv.reader(request_file)

            next(reader)
            request_list = []    
            for row_list in reader:
        
                # If the current row is not blank,
                # append it to the request_list.
                if len(row_list) != 0:

                    # Append one row from the CSV
                    # file to the compound list.
                    request_list.append(row_list)
            #print(request_list)       
        
        print()
        print('Inkom Emporium')
        print()
        #'for' loop to find the requested product in the dictionary 
        quantity_total = 0
        subtotal = 0
        for request, Quantity in request_list:
            
            value = products_dict[request]
            name = value[1]
            price = float(value[2])
            
            if day == "Tuesday" or day =="Wednesday":
                price = round(price - (price*0.1), 2)
                quantity_total += int(Quantity)
                subtotal += float(price) * int(Quantity)
                
                print(f'{name}: {Quantity} $ {price}')
            else :
                
                quantity_total += int(Quantity)
                subtotal += float(price) * int(Quantity)
                
                print(f'{name}: {Quantity} $ {price}')
            
        tax = subtotal*0.06
        total = round(subtotal + tax, 2) 
        print()
        print(f'Number of Items: {quantity_total}') 
        print(f'Subtotal: {subtotal:.2f}') 
        print(f'Sales Tax: {tax:.2f}')  
        print(f'Total: {total}')
        print()
        print('Thank you for shopping at the Inkom Emporium.')

        # Use an f-string to print the current
        # day of the week and the current time.
        print(f"{current_date_and_time:%a %b %d %X %Y}")

    except KeyError as keyerror:
        print(f'Error: unknown product ID in the request.csv file {keyerror}')

    except FileNotFoundError as not_found_err:
        print('Error: missing file')
        print(not_found_err)

    except PermissionError as perm_err:
        print(perm_err)

    

        
def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    dictionary = {}


    with open(filename, "rt") as csv_file:

        reader = csv.reader(csv_file)


        # This statement skips
        # the first row of the CSV file.
        next(reader)


        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(row_list) != 0:

                # From the current row, retrieve the data
                # from the column that contains the key.
                #name = row_list[1]
                #price = row_list[2]
                key = row_list[key_column_index]

                # Store the data from the current
                # row into the dictionary.
                dictionary[key] = row_list
                #dictionary[key] = [name, price]

    # Return the dictionary.
    return dictionary


if __name__ =='__main__':
    main()