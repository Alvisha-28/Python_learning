#moving zeroes at the end of the array while maintaining the order of non-zero elements
def move_zeroes(arr):
    non_zero_index = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_index] = arr[i]
            non_zero_index += 1
    for i in range(non_zero_index, len(arr)):
        arr[i] = 0
    return arr
arr = [0, 1, 0, 3, 12]
result = move_zeroes(arr)
print("Array after moving zeroes:", result)

class Solution:
    def moveZeroes(self, nums):
        i = 0  # position to place next non-zero

        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
