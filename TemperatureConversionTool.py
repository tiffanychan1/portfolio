# Convert temperatures between Fahrenheit and Celsius

def temp_conversion():
    print("Temperature Conversion Tool \n")
    
    while True:
    
        # user-input temperature
        while True:
            try:
                temp = input("What is the temperature in degrees? ")
                degrees = float(temp)
                break
            except ValueError:
                print('Please only type numbers')
    
        # user-input scale
        while True:
            fc = input("Is this in Fahrenheit or Celsius? (type F or C) ")
            scale = fc.upper()
            if scale == 'F' or scale == 'C':
                break
            else:
                print("Please only type F or C")
        
        # conversion equations
        if scale == 'F':
            cels = (degrees - 32) * (5 / 9)
            cels = round(cels, 2)
            print(f"The equivalent temperature in Celsius is {cels} degrees")
        if scale == 'C':
            fahr = degrees * (9 / 5) + 32
            fahr = round(fahr, 2)
            print(f"The equivalent temperature in Fahrenheit is {fahr} degrees")
            
        # user-input whether to repeat process
        while True:
            repeat = input("\nWould you like to perform another conversion? (type Y or N) ")
            answer = repeat.upper()
            if answer == 'Y' :
                print()
                break
            elif answer == 'N':
                return
            else:
                print("Please only type Y or N")
            
temp_conversion()
