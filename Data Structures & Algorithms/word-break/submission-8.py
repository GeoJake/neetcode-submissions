class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        words = set(wordDict)
        memo = {len(s) : True}

        def dfs(i: int) -> bool:

            if i in memo:
                return memo[i]
            
            for w in words:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    if dfs(i + len(w)):
                        memo[i] = True
                        return memo[i]
            
            memo[i] = False
            return memo[i]
        
        return dfs(0)