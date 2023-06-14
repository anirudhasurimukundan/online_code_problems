# Find if 2 strings are anagrams or not
# We use Counter function from the collections library to solve this problem
# Counter neatly identifies the number of occurrence of each alphabet in each string and output as dictionary
# Logic: if the Counters of 2 strings are same/equal, then they strings are anagrams else not
# Time complexity: O(n) where n is the number of characters in each string
# Memory space complexity: O(1) since we store only the 2 strings and not create any new variable

from collections import Counter # for checking the number of times each alphabet occurs in a string

if __name__ == "__main__":
    string1 = "eat" # "bad" #"silent"
    string2 = "ate" # "dad" #"listen"
    if(len(string1) != len(string2)):
        print(f"{string1} and {string2} are not of equal lengths")
    else:
        if(Counter(string1) == Counter(string2)):
            print(f"{string1} and {string2} are anagrams")
        else:
            print(f"{string1} and {string2} are not anagrams")

