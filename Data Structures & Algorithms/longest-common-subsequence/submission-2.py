class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        #   c r a b t
        # c 1 1 1 1 1
        # a 1 1 2 2 2
        # t 1 1 2 2 3

        if len(text1) > len(text2):
            text1, text2 = text2, text1

        m, n = len(text1), len(text2)

        dp = [[0] * (m+1) for _ in range(n+1)]

        for r in range(n-1, -1, -1):
            for c in range(m-1, -1, -1):
                if text1[c] == text2[r]:
                    dp[r][c] += 1 + dp[r+1][c+1]
                else:
                    dp[r][c] = max(dp[r+1][c], dp[r][c+1]) 
                
        
        print(dp)
        
        return dp[0][0]