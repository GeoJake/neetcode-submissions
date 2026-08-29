class Solution:
    def countSubstrings(self, s: str) -> int:
        res = []
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and ((j - i + 1) <= 2 or dp[i+1][j-1]):
                    res.append(s[i:j+1])
                    dp[i][j] = True

        return len(res)