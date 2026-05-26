#linear search along with time complexity
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
arr = [5, 3, 2, 8, 1]
target = 2
result = linear_search(arr, target)
if result != -1:
    print(f"Element {target} found at index: {result}")
else:
    print(f"Element {target} not found in the array.")
    