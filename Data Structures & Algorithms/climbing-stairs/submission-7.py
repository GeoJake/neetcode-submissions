class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        def helper(n: int) -> int:
            if dp[n] > 0:
                return dp[n]

            dp[n] = helper(n - 2) + helper(n - 1)
            return dp[n]

        return helper(n)