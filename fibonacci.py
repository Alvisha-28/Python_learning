#fibonacci series number printing using recursion
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series
number = int(input("Enter the number of Fibonacci terms to generate: "))
print(f"The first {number} terms of the Fibonacci series are: {fibonacci(number)}")




