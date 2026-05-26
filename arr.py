def find_max(arr):
    max_value = arr[0]
    for num in arr:
        if num > max_value:
            max_value = num
    return max_value
def find_min(arr):
    min_value = arr[0]
    for num in arr:
        if num < min_value:
            min_value = num
    return min_value

arr = [17,45,67,89]
res1 = find_max(arr)
res2 = find_min(arr)    
print("Maximum value:", res1)
print("Minimum value:", res2)