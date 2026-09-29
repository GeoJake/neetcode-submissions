class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = [-1] * len(cost)

        def helper(n : int):
            if n >= len(cost):
                return 0

            if memo[n] > -1:
                return memo[n]

            memo[n] = cost[n] + min(helper(n + 1), helper(n + 2))
            return memo[n]

        return min(helper(0), helper(1))