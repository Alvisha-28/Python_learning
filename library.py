#books in library to search for a book using recursion function
def match(n,target):
    if n == 0:
        return False
    elif n == target:
        return True
    else:
        return match(n - 1, target)
if __name__ == "__main__":
    n = int(input("Enter the number of books in the library: "))
    target = int(input("Enter the book number to search for: "))
    if match(n, target):
        print(f"Book number {target} is found in the library.")
    else:
        print(f"Book number {target} is not found in the library.")
        
