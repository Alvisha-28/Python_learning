#check whether a number is a strong number or not
import math

n = int(input("Enter a number: "))
s = 0
temp = n

while temp > 0:
    d = temp % 10
    s += math.factorial(d)
    temp //= 10

print("Strong number" if s == n else "Not a strong number")
