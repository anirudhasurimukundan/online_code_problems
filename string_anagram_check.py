from collections import Counter # for checking the number of times each alphabet occurs in a string

if __name__ == "__main__":
    string1 = "eat" # "bad" #"silent"
    string2 = "ate" # "dad" #"listen"
    if(Counter(string1) == Counter(string2)):
        print(f"{string1} and {string2} are anagrams")
    else:
        print(f"{string1} and {string2} are not anagrams")

