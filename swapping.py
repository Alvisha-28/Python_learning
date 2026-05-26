
#swapping two numbers without using a temporary variable using functions
#def swap(a, b):
    #a = a + b
    #b = a - b
    #a = a - b
    #return a,b
# Example usage:
#num1 = 65
#num2 = 10
#print("Before swapping: num1 =", num1, "num2 =", num2)
#num1, num2 = swap(num1, num2)
#print("After swapping: num1 =", num1, "num2 =", num2)

# input two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\nBefore swapping:")
print("a =", a, " address =", id(a))
print("b =", b, " address =", id(b))

# swapping
a, b = b, a

print("\nAfter swapping:")
print("a =", a, " address =", id(a))
print("b =", b, " address =", id(b))





