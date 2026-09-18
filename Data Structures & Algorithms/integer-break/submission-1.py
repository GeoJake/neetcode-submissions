class Solution:
    def integerBreak(self, n: int) -> int:
        
        memo = [0] * n 
        memo[0] = memo[1] = 1
        
        def dfs(i: int) -> int:
            if memo[i]:
                return memo[i]

            maxVal = i
            for j in range(1, i):
                maxVal = max(maxVal, dfs(j) * dfs(i - j))
            memo[i] = maxVal

            return memo[i]

        maxVal = 0
        for i in range(1, n):
            val = dfs(i) * dfs(n - i)
            maxVal = max(maxVal, val)

        return maxVal