class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        l = 0
        length = 0
        seen = {} # character:index
        for r in range(len(s)):
            c = s[r]
            if c in seen and seen[c] >= l:
                l += seen[c] + 1
            else:
                length = max(length, r - l + 1)
            seen[c] = r
        return length

if __name__ == "__main__":
    sol = Solution;
    s = "abcabcbb"
    s = "bbbbb"
    #s = "pwwkew"
    s = " "
    #s = "dvdf"
    print(sol.lengthOfLongestSubstring(sol, s))
