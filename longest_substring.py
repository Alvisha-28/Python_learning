#Longest Substring Without Repeating Characters
def length_of_longest_substring(s):
    char_index = {}
    longest = 0
    start = 0

    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = i
        longest = max(longest, i - start + 1)

    return longest  
# Example usage:
input_string = "abcabcbb"
print("Length of the longest substring without repeating characters:", length_of_longest_substring(input_string))
