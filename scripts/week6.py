
print('Decide where to travel and learn more about the place!')

#first level
continent = input('Do you want to travel to SOUTH AMERICA or OCEANIA or EUROPE? ')

if continent.lower() == 'south america':
    print('')
    #second level
    country = input('Do you want to travel to Brazil or Argentina or Peru? ') 

    if country.lower() == 'brazil':
        print('Happy travels to Brazil, the country of the "jogo bonito"!')
        print('')
        #third level
        date = input('What part of Brazil would you like to travel to? RIO DE JANEIRO or PORTO ALEGRE ')

        if date.lower() == 'rio de janeiro':
            print('The main attraction is Christ the Redeemer.')

        elif date.lower() == 'porto alegre':
            print('We suggest you visit the Farroupilha Park!')
        else : 
            print('There is no travel to that part of Brazil')     

    elif country.lower() == 'argentina':
        print('Very good choice! it goes to the country of the "asado" and the famous "mates"!')
        print('')

        date = input('When do you want to travel? AUGUST or SEPTEMBER ')

        if date.lower() == 'august':
            print('You will need to bring a good coat!')

        elif date.lower() == 'september':
            print('The best time to travel to Argentina, the beginning of spring!')
        else :
            print(f'We have no flights in {date}')    

    elif country.lower() == 'peru':
        print('You can not leave Peru without visiting Machupichu.')    

    else :
        print(f'We cannot take you to {country}')    

elif continent.lower() == 'oceania':
    print('')

    country = input('Do you want to travel to NEW ZEALAND or AUSTRALIA? ')

    if country.lower() == 'new zealand':
        print('Happy travel to new zealand, you have to go see Rugby.')

    elif country.lower() == 'australia':
        print('Happy travels to Australia, watch out for the kangaroo!')

    else :
        print(f'We cannot take you to {country}')    

elif continent.lower() == 'europe':
    print('') 
    #second level
    country = input('Do you want to travel to ITALY or SPAIN? ')

    if country.lower() == 'italy':
        print('Happy travel to Italy, "buon appetito"')

    elif country.lower() == 'spain':
        print('We recommend a visit to Barcelona')

    else :
        print(f'We cannot take you to {country}')
else :
    print('')
    print(f'We have no flights to {continent}')                         

