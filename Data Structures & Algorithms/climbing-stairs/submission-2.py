class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * n

        def helper(i):
            if i >= n:
                return i == n

            if dp[i] != -1:
                return dp[i]

            dp[i] = helper(i + 1) + helper(i + 2)
            return dp[i]
    
        return helper(0)