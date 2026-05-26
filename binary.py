#binary search 
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
input_target = int(input("Enter the target element to search: "))

result = binary_search(arr, input_target)
if result != -1:
    print(f"Element {input_target} found at index: {result}")
else:
    print(f"Element {input_target} not found in the array.")



