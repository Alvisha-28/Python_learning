#sum of natural numbers using recursion
def sum_natural(n):
    if n <= 0:
        return 0
    else:
        return n + sum_natural(n - 1)
number = int(input("Enter a positive integer: "))
result = sum_natural(number)
print(f"The sum of the first {number} natural numbers is: {result}")
