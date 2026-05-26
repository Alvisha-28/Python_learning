#print the elements at odd index in a list and analyze the time complexity of the code

def odd_index_elements(lst):
    odd_index_lst = []
    for i in range(1, len(lst), 2):
        odd_index_lst.append(lst[i])
    return odd_index_lst

# Example usage
my_list = input("Enter a list of elements separated by space: ").split()
result = odd_index_elements(my_list)
print("Elements at odd index:", result)
# Time complexity: O(n/2) which simplifies to O(n) where n is the number of elements in the input list. 
