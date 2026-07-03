class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        min_diff = max(nums) - min(nums)
        for r in range(k-1, len(nums)):
            min_diff = min(min_diff, nums[r]-nums[r-k+1])
        
        return min_diff