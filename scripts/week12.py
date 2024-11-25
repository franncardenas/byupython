


chosen_year = input("Enter the year of interest: ")
chosen_country = input("Enter the country of interest: ")
print()
chosen_year = int(chosen_year)


#Load the dataset in your Python program
with open('life-expectancy.csv') as life_expectancy:

    
    next(life_expectancy)
    #file = life_expectancy.read()

    lowest_value = 99999
    highest_value = 0
    min_life = 9999
    max_life = 0
    average_ages = 0
    average_age = 0
    count = 0
    min_life2 = 9999
    max_life2 = 0
    average_ages2 = 0
    average_age2 = 0
    count2 = 0

    for line in life_expectancy:

        line = line.strip()
        parts = line.split(",")
        #parts[3] = parts[3].strip()

        citys = parts[0]
        years = int(parts[2])
        value_life = float(parts[3])
        
        
        #What is the year and country that has the lowest life expectancy in the dataset?
        if value_life < lowest_value:
            
            lowest_value = value_life
            city = citys
            year = years
            #print(lowest_value)


        #What is the year and country that has the highest life expectancy in the dataset?
        if value_life > highest_value:
            
            highest_value = value_life
            city2 = citys
            year2 = years
            #print(highest_value)

        #Year of interest
        if chosen_year == years:
            average_ages += value_life
            count = count + 1

            average_age = average_ages/count

             
            #max life expectancy (year)
            if value_life > max_life :
                
                max_life = value_life
                max_city = citys


            #min life expectancy (year)
            if value_life < min_life :
                
                min_life = value_life
                min_city = citys

            
        #Country interest
        if chosen_country.lower() == citys.lower():
            average_ages2 += value_life
            count2 = count2 + 1

            average_age2 = average_ages2/count2

            ##max life expectancy (country)
            if value_life > max_life2 :
                
                max_life2 = value_life
                max_year = years

            #min life expectancy (country)
            if value_life < min_life2 :
                
                min_life2 = value_life
                min_year = years



    

    print(f"The overall max life expectancy is: {highest_value:.2f} from {city2} in {year2}")
    print(f"The overall min life expectancy is: {lowest_value:.2f} from {city} in {year}")
    print()


    print(f"For the year {chosen_year}: ")
    print(f"The average life expectancy across all countries was: {average_age:.2f}")
    print(f"The max life expectancy was in {max_city} with {max_life:.2f}")
    print(f"The min life expectancy was in {min_city} with {min_life:.2f}")
    print()


    print(f"For the year {chosen_country}: ")
    print(f"The average life expectancy was: {average_age2:.2f}")
    print(f"The max life expectancy was in {max_year} with {max_life2:.2f}")
    print(f"The min life expectancy was in {min_year} with {min_life2:.2f}")    
    

