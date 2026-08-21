class Solution:
    def rob(self, nums: List[int]) -> int:        
        n = len(nums) - 1
        memo = [-1] * len(nums)

        def dfs(i):
            if i < 0:
                return 0    
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(nums[i] + dfs(i - 2), dfs(i - 1))
            return memo[i]

        return dfs(n)