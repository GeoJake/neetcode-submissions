class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numToLetter = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z'],
        }

        out = []

        def dfs(subset, index):
            if index >= len(digits):
                out_str = "".join(subset.copy())
                if len(out_str):
                    out.append(out_str)
                return
            
            for c in numToLetter[digits[index]]:
                subset.append(c)
                dfs(subset, index + 1)
                subset.pop()
        
        dfs([], 0)

        return out
        