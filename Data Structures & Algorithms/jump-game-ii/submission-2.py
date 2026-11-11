class Solution:
    def jump(self, nums: List[int]) -> int:
        res = farthest = current_end = 0
        
        for i in range(len(nums) - 1):
            farthest = max(farthest, nums[i] + i)
            if i == current_end:
                current_end = farthest
                res += 1

        return res