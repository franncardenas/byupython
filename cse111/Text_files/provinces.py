

def main():
    # Read the contents of a text file
    # named plants.txt into a list.
    provinces_list = read_list("Text_files/provinces.txt")
    

    # Print the entire list.
    print(provinces_list)

    #Remove the firts element from the list
    provinces_list.pop(0)

    #Remove the last element from the list 
    provinces_list.pop()

    # Replace all occurrrences of "AB" with "Alberta".
    for i in range(len(provinces_list)):
        if provinces_list[i] == "AB":
            provinces_list[i] = "Alberta"

    # Call the list.count method which will count the
    # number of times that Alberta appears in the list.
    count = provinces_list.count("Alberta")

    print()
    print(f"Alberta occurs {count} times in the modified list.")
    

def read_list(filename):

    # Create an empty list that will store
    # the lines of text from the text file.
    text_list = []

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, 'rt') as text_file:

        for line in text_file :

            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = line.strip()

            # Append the clean line of text
            # onto the end of the list.
            text_list.append(clean_line)



    return text_list


if __name__ == "__main__":
    main()