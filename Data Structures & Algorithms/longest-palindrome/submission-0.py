class Solution:
    def longestPalindrome(self, s: str) -> int:
        chars = {}

        res = 0
        for c in s:
            if c not in chars:
                chars[c] = 0
            chars[c] += 1
            if not chars[c] % 2:
                res += 2

        return res + (res < len(s))