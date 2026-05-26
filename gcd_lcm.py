#write a two functions that calculate the greatest common divisor (GCD) and least common multiple (LCM) of two numbers.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return (a * b) // gcd(a, b)
# Example usage:
num1 = 12
num2 = 15
print("GCD of", num1, "and", num2, "is:", gcd(num1, num2))
print("LCM of", num1, "and", num2, "is:", lcm(num1, num2))
