#n th element in array
'''def nth_element(arr, n):
   return arr[n-1]
if __name__ == "__main__":
   n = int(input("Enter the position of the element to retrieve: "))
   arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))
   print("nth element in the array is:", nth_element(arr, n))'''
   
def find(n,arr):
    if n<=len(arr)and n>0:
        return arr[n-1]
    elif(n>= - len(arr) and n<0):
        return arr[n]
    else:
        return "Index out of range"
if __name__ == "__main__":
    n = int(input("Enter the position of the element to retrieve: "))
    arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))
    print("nth element in the array is:", find(n,arr))
    