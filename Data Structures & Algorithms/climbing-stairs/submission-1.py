class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 2

        def helper(n: int) -> int:
            if n == 1:
                return 1

            if n == 2:
                return 2

            if dp[n] > 0:
                return dp[n]

            dp[n] = helper(n-1) + helper(n-2)
            return dp[n]
    
        return helper(n)
        