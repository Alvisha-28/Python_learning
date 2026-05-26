#reverse a string using do while loop
s = input("enter a string: ")
rev = ""
i = len(s) - 1
while True: 
    rev += s[i]
    i -= 1
    if i < 0:
        break
print("reversed string is: ", rev)

