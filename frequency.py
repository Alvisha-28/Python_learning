from collections import Counter
s = input("enter a string:").lower()
filtered = [char for char in s if char.isalpha()]
frequency = Counter(filtered)
for char, count in frequency.items():
    print(f"{char}: {count}")