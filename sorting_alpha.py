#sort the names of fruits alphabetically
fruits = ["banana", "apple", "grape", "orange", "kiwi"]
n = len(fruits)
for i in range(n):
    for j in range(0, n-i-1):
        if fruits[j] > fruits[j+1]:
            fruits[j], fruits[j+1] = fruits[j+1], fruits[j]
print("Fruits sorted alphabetically:", fruits)
