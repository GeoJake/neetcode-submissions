class Solution:
    def rob(self, nums: List[int]) -> int:        

        memo = [0] * len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0
            
            if memo[i] > 0:
                return memo[i]

            next_house = dfs(i + 1)
            this_house = nums[i] + dfs(i + 2)
            memo[i] = max(this_house, next_house)
            return memo[i]

        return dfs(0)