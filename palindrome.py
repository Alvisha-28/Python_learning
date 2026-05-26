s = str(input("Enter a string: "))
l = 0
r = len(s) - 1
is_palindrome = True
while l < r:
    if s[l] != s[r]:
        is_palindrome = False
        break
    l += 1
    r -= 1
if is_palindrome:
    print(f'"{s}" is a palindrome.')
else:
    print(f'"{s}" is not a palindrome.')
    print(f'Reversed: "{s[::-1]}"')