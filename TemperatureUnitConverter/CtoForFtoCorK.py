gvmeweather = input("First you select, Which unit do you want to convert from? please press (C/F/K): ").lower()

if gvmeweather == "f":
    gvmeconvt = input("Second select, What unit do you want to convert to? please press (C/K): ").lower()
    if gvmeconvt == "c":
        try:
            wethr = int(input("Can you write the weather in fahrenheit as a number: "))
            print("Weather is {0:.2f} °C".format((wethr-32)*5/9))
        except ValueError:
            print("Bye Bye, Next Time")
        exit()    
    elif gvmeconvt == "k":
        try:
            wethr = input("Can you write the weather in fahrenheit as a number: ")
            print("Weather is {0:.2f} K".format((wethr-32)*5/9 + 273.15))
        except ValueError:
            print("Bye Bye, Next Time")
        exit()   
    else:
        print("Go and keep playing in the sand")
elif gvmeweather == "c":
    gvmeconvt = input("Second select, What unit do you want to convert to? please press (F/K): ").lower()
    if gvmeconvt == "f":
        try:
            wethr = int(input("Can you write the weather in celsius as a number: "))
            print("Weather is {0:.2f} °F".format(wethr*9/5+32))
        except ValueError:
            print("Bye Bye, Next Time")
        exit()    
    elif gvmeconvt == "k":
        try:
            wethr = input("Can you write the weather in celsius as a number: ")
            print("Weather is {0:.2f} K".format(wethr+273.15))
        except ValueError:
            print("Bye Bye, Next Time")
        exit()
    else:
        print("Go and keep playing in the sand")
elif gvmeweather == "k":
    gvmeconvt = input("Second select, What unit do you want to convert to? please press (C/F): ").lower()
    if gvmeconvt == "f":
        try:
            wethr = int(input("Can you write the weather in kelvin as a number: "))
            print("Weather is {0:.2f} °F".format((wethr-273.15)*9/5 + 32))
        except ValueError:
            print("Bye Bye, Next Time")
        exit()
    elif gvmeconvt == "c":
        try:
            wethr = int(input("Can you write the weather in kelvin as a number: "))
            print("Weather is {0:.2f} °C".format(wethr-273.15))
        except ValueError:
            print("Bye Bye, Next Time")
        exit()
    else:
        print("Go and keep playing in the sand")        
else:
    print("One day, I hope you add this unit of temperature measurement")