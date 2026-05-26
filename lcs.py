def lcs(x,y):

    m = len(x)
    n = len(y)
    dp = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

    return dp[m][n]
x = input("Enter the first string: ")
y = input("Enter the second string: ")
result = lcs(x, y)
print("Length of LCS is", result)
