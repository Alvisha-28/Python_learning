# You are given an array containing n elements where each element is either a policeman ('P') 
# or a thief ('T'). Each policeman can catch only one thief, and a policeman cannot catch a thief 
# who is more than K units away from him. Your task is to find the maximum number of 
# thieves that can be caught by the policemen. 

# The first line contains an integer n, the size of the array. 
# The second line contains the integer K, the maximum distance a policeman can catch a thief. 
# The third line contains a string of length n containing characters 'P' and 'T' (e.g., "PTTPPT").
from collections import deque
n = int(input("Enter the size of the array: "))
K = int(input("Enter the maximum distance K: "))
array = input("Enter the array (string of 'P' and 'T'): ")

def catch_theives(arr, n, k):
    police = deque()
    thieves = deque()
    count = 0
    for i in range(n):
        if arr[i] == 'P':
            police.append(i)
        elif arr[i] == 'T':
            thieves.append(i)
    while police and thieves:
        p_index = police[0]
        t_index = thieves[0]
        if abs(p_index - t_index) <= k:
            count += 1
            police.popleft()
            thieves.popleft()
        elif p_index < t_index:
            police.popleft()
        else:
            thieves.popleft()
    return count
result = catch_theives(array, n, K)
print("maximum  number of thieves that can be caught:", result )

    

        