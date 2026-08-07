class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numToLetter = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        out = []

        def dfs(subset, index):
            if len(subset) == len(digits):
                out.append(subset)
                return
            
            for c in numToLetter[digits[index]]:
                dfs(subset + c, index + 1)
        
        if digits:
            dfs("", 0)

        return out
        