
    #write a program to print sum of the multiple of three and sum of the multiple of five in a given range
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))   
sum_of_multiples_of_three = 0
sum_of_multiples_of_five = 0
for i in range(start, end + 1):
    if i % 3 == 0:
        sum_of_multiples_of_three += i
    if i % 5 == 0:
        sum_of_multiples_of_five += i
print("Sum of multiples of 3: ", sum_of_multiples_of_three)
print("Sum of multiples of 5: ", sum_of_multiples_of_five)
