class Solution:
    def firstRepeatedString(self, s):
        l = len(s)
        res = []
        for c in s:
            if c not in res:
                res.append(c)
            else:
                return(f"Repeated character {c} found")
        return (f"No repeated character found")

if __name__ == "__main__":
    sol = Solution;
    s = "bb"
    print(sol.firstRepeatedString(sol, s))
