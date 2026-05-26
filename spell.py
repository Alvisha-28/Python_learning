# Hemanth, a young wizard, is learning how to craft powerful spells. Each spell is represented 
# as a string of letters, where the frequency of certain letters determines the spell's strength. To 
# create an effective spell, Hemanth needs to identify the letters that appear at least a certain 
# number of times. 
# The wizard's task is to find and list these magical letters in alphabetical order to ensure his 
# spell is strong and organized. Help Hemanth by writing a program that identifies these letters. 
# Hemanth is given a string S, representing a spell, and an integer K. Your task is to find all 
# characters in the spell that appear at least K times and print them in alphabetical order. 
from collections import Counter
N,K = map(int, input("Enter the length of the spell and the minimum frequency: ").split())
spell = input("Enter the spell: ")
frequency = Counter(spell)
result = [char for char, count in frequency.items() if count >= K]
result.sort()
print("Characters that appear at least", K, "times:")
for char in result:
    print(char)

    