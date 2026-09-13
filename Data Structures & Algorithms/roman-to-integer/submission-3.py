class Solution:
    def romanToInt(self, s: str) -> int:
        
        res = 0
        i = 0

        romToInt = {"I": 1, "V": 5, "X": 10, 
                    "L": 50, "C": 100, "D": 500,
                    "M": 1000}

        for i in range(len(s)):
            if i + 1 < len(s) and romToInt[s[i]] < romToInt[s[i + 1]]:
                res -= romToInt[s[i]]
            else:
                res += romToInt[s[i]]

        return res