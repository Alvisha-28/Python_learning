
# def fib(n):
#     if(n==1 or n==0):
#         return n
#     return fib(n-1)+fib(n-2)
# n = int(input("Enter the number: "))
# print("Fibonacci number is", fib(n))
# how to optimize the above code using dynamic programming
# def fib(n, dp):
#     if(n==1 or n==0):
#         return n
#     if dp[n] != -1:
#         return dp[n]
#     dp[n] = fib(n-1, dp) + fib(n-2, dp)
#     return dp[n]
# n = int(input("Enter the number: "))
# dp = [-1] * (n + 1)
# print("Fibonacci number is", fib(n, dp))
#using tabulation
# def fib(n):
#     dp = [0] * (n + 1)
#     dp[1] = 1
#     for i in range(2, n + 1):
#         dp[i] = dp[i - 1] + dp[i - 2]
#     return dp[n]
# n = int(input("Enter the number: "))
# print("Fibonacci number is", fib(n))
dp =[-1] * 31
print()
print(dp)
def fib(n):
    if(n==1 or n==0):
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = fib(n-1) + fib(n-2)
    return dp[n]
n = int(input("Enter the number: "))
print("Fibonacci number is", fib(n))
print(dp)
