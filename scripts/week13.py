

# Allow the user to enter the temperature in Celsius of Fahrenheit
temp = int(input('What is the temperature?: '))
which_temp = str(input('Fahrenheit or Celsius (F/C)?: '))

wind = 5

# Write a function to calculate and return the wind chill based on a given temperature and wind speed.
def get_wind_chill(wind, temp):

    wind_chill = 35.74 + 0.621*temp - 35.75*(wind**0.16) + 0.4275*temp*(wind**0.16)
    return wind_chill
    

# Write a function to convert from Celsius to Fahrenheit.    
def convert_temperature(temp):

    temp_f = (temp*9/5) + 32
    return temp_f


# If they provide it in Celsius, first convert it to Fahrenheit before using the formula above.
if which_temp.upper() == 'C':

    temp_convert = convert_temperature(temp)
    # Loop through wind speeds from 5 to 60 miles per hour, incrementing by 5
    while wind <= 60:

        print(f'At temperature {temp_convert:.1f}F, and wind speed {wind} mph, the windchill is: {get_wind_chill(wind,temp_convert):.2f}F') #Display the wind chill value to 2 decimals of precision.
        wind += 5


else :
    # Loop through wind speeds from 5 to 60 miles per hour, incrementing by 5
    while wind <= 60:

        print(f'At temperature {temp:.1f}F, and wind speed {wind} mph, the windchill is: {get_wind_chill(wind,temp):.2f}F') #Display the wind chill value to 2 decimals of precision.
        wind += 5



















