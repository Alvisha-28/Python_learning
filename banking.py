#banking system computes a check digit by repeatedly summing the digits of a number until a single digit is obtained.
def compute_check_digit(number):
    while number >= 10:
        number = sum(int(digit) for digit in str(number))
    return number   
number = int(input("Enter a number: "))
check_digit = compute_check_digit(number)
print("The check digit is:", check_digit)
