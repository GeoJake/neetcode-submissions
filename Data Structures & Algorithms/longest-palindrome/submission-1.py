class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        res = 0
        for c in s:
            if c in seen:
                res += 2
                seen.remove(c)
            else:
                seen.add(c)
        
        return res + 1 if seen else res