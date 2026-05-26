#find the number of non-repeating elements in an array and also print the non-repeating elements
def count_non_repeating(arr):
    count = 0
    for num in arr:
        if arr.count(num) == 1:
            count += 1
    return count    
arr = [1, 2, 3, 4, 2, 5, 1] 
result = count_non_repeating(arr)
print("Number of non-repeating elements:", result)
print("Non-repeating elements:", [num for num in arr if arr.count(num) == 1])
