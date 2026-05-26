temp_in_cel = float(input("Enter the temperature in Celsius: "))
temp_in_fahr = (temp_in_cel * 9/5) + 32
print("The temperature in Fahrenheit is: ", temp_in_fahr)
temp_in_kelvin = temp_in_cel + 273.15
print("The temperature in Kelvin is: ", temp_in_kelvin)
if temp_in_cel <0:
    print("The temperature is below freezing point.")
elif temp_in_cel < 15:
    print("The temperature is moderate.")
elif temp_in_cel < 30:
        print("The temperature is warm.")       
    
else:    print("The temperature is above normal.")  
