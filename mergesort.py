#merge sort 
''''def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Sorted array:", arr)'''


from heapq import merge


def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list

    mid = len(unsorted_list) // 2
    left_half = merge_sort(unsorted_list[:mid])
    right_half = merge_sort(unsorted_list[mid:])

    return merge(left_half, right_half)
left_list = merge_sort([38, 27, 43, 3, 9, 82, 10])
right_list = merge_sort([38, 27, 43, 3, 9, 82, 10])
print("Sorted array:", merge(left_list, right_list))

    