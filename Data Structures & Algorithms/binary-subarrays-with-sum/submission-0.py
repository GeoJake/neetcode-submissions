class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        prefix_sum[0] = 1
        total, res = 0, 0

        for num in nums:
            total += num
            if total >= goal:
                res += prefix_sum[total - goal]
            prefix_sum[total] += 1
        
        return res