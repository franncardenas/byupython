def main():
    try:
        # Create and print a list named fruit.
        fruit_list = ["pear", "banana", "apple", "mango"]
        print(f"original: {fruit_list}")

        #reverse:
        fruit_list.reverse()
        print(f"reverse: {fruit_list}")

        #append orange:
        fruit_list.append('orange')
        print(f'append orange: {fruit_list}')

        #insert cherry:
        fruit_list.insert(1, 'cherry')
        print(f'insert cherry: {fruit_list}')

        #remove banana:
        fruit_list.remove('banana')
        print(f'remove banana: {fruit_list}')

        #pop orange:
        fruit_list.pop()
        print(f'pop orange: {fruit_list}')

        #sorted:
        fruit_list.sort()
        print(f'sorted: {fruit_list}')

        #cleared: 
        fruit_list.clear()
        print(f'cleared: {fruit_list}')
    except IndexError as index_err:
        print(type(index_err).__name__, index_err, sep=": ")










if __name__== '__main__':
    main()