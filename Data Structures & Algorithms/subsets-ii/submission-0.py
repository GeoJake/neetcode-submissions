class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        def dfs(subset, idx):
            if idx >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[idx])
            dfs(subset, idx + 1)

            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1

            subset.pop()
            dfs(subset, idx + 1)
        
        dfs([], 0)

        return res