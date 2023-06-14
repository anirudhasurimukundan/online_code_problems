# Given two strings s and t, check if they are anagrams
# Logic: count the character repetition in each string and assign to a list
# If the lists for strings s and t are same, then s and t are anagrams else not
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count_s = [0] * 26
        count_t = [0] * 26
        for c in s:
            count_s[ord(c) - ord("a")] += 1
        for c in t:
            count_t[ord(c) - ord("a")] += 1
        
        return(count_s == count_t)

if __name__ == "__main__":
    sol = Solution;
    s = "rat"
    t = "tara"
    print(sol.isAnagram(sol, s, t))


### Surprisingly a slightly longer time consuming approach (above approach 34 ms while below approach is 43 ms)
#class Solution(object):
#    def isAnagram(self, s, t):
#        """
#        :type s: str
#        :type t: str
#        :rtype: bool
#        """
#        return(Counter(s) == Counter(t))
