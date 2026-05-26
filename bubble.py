#bubble sort dry run the user will input the numbers and the program will sort them using bubble sort algorithm

'''arr = input("Enter numbers separated by space: ").split()
for i in range(len(arr)):
    arr[i] = int(arr[i])    
n = len(arr)    
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print("Sorted array:", arr)'''

string_input = input("Enter a string to sort: ")
arr = list(string_input)    
n = len(arr)
flag = True
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            flag = False
    if flag:
        break
print("Sorted array:", arr)

