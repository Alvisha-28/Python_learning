#power_of_three

def is_power_of_three(n):
    if n <= 0:
        return False
    while n % 3 == 0:
        n //= 3
    return n == 1

number = int(input("Enter a number: "))
if is_power_of_three(number):
    print(f"{number} is a power of three.")
else:
    print(f"{number} is not a power of three.")
        