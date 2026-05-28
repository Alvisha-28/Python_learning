# #palindrome and print the string in reverse order
# def is_palindrome(s):
#     cleaned_s = ''.join(s.split()).lower()
#     return cleaned_s == cleaned_s[::-1]
# input_string = input("Enter a string: ")
# if is_palindrome(input_string):
#     print(f'"{input_string}" is a palindrome.')
# else:
#     print(f'"{input_string}" is not a palindrome.')
#     print(f'Reversed: "{input_string[::-1]}"')
    
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]