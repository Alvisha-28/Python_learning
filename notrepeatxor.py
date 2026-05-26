arr = [2, 3, 2, 4, 4]
def single_non_repeating(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

print(single_non_repeating(arr))