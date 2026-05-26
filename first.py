unit = int(input("Enter a number: "))
if(unit <=100):
    amount = unit * 1.50
    print(amount)
    print("The number is less than or equal to 100")
elif(unit<= 200):
    amount = 100*1.50 + (unit - 100) * 2.50
    print(amount)
    print("The number is greater than 100 and less than or equal to 200")
else:
    amount = 100*1.50 + 100*2.50 + (unit - 200) * 3.50
print(amount)
print("The number is greater than 200")