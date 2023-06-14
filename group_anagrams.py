from collections import Counter,defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagram_list = defaultdict(list) # {} # hashmap mapping character count to list of anagrams as sublist 
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            anagram_list[tuple(count)].append(s)
        return anagram_list


if __name__ == "__main__":
    sol = Solution;
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(sol.groupAnagrams(sol, strs))
