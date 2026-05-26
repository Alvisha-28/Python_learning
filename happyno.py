#print the happy number
def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1   
number = int(input("Enter a number: "))
if is_happy(number):

    print(f"{number} is a happy number.")
else:
    print(f"{number} is not a happy number.")
    
