n = int(input("Enter number of rows: "))

for i in range(n):
    num = 1
    
    # print spaces for alignment
    print(" " * (n - i), end="")
    
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    
    print()
    #it is a pattern where each value is the sum of the two values directly above it in the previous row. The first and last value of each row is always 1. The number of values in each row corresponds to the row number, starting with 0 for the topmost row.
    #widely used in mathematics