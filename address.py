
#adding and then printing an address malloc concept in python

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
malloc = [0] * 10  # Simulating memory allocation
print("\nMemory addresses of malloc array:")
for i in range(len(malloc)):
    print(f"malloc[{i}] address = {id(malloc[i])}")
        