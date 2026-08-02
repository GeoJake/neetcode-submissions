class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(total, subset, idx):
            if total > target:
                return
            
            if total == target:
                res.append(subset.copy()) 
                return

            if idx >= len(nums):
                return
            
            val = nums[idx]
            subset.append(val)
            total += val

            helper(total, subset, idx)

            idx += 1
            subset.pop()
            total -= val

            helper(total, subset, idx)

        helper(0, [], 0)

        return res