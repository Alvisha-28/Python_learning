# Longest Common Prefix
def longest_common_prefix(strs):
    if not strs:
        return ""
    
    prefix = ""
    for i in range(len(strs[0])):
        char = strs[0][i]
        for s in strs[1:]:
            if i >= len(s) or s[i] != char:
                return prefix
        prefix += char
    return prefix

# Example usage
strings = ["flower", "flow", "flight"]
print(longest_common_prefix(strings))  # Output: "fl"           
