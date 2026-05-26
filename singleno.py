#single number given a non empty list where every element appears twice except for one find that single one
def single_non_repeating(arr):
    result = 0
    for num in arr:
        result ^= num
    return result
arr = [2, 3, 2, 4, 4]
print(single_non_repeating(arr))
