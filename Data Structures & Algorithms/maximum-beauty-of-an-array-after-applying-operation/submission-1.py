class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:

        nums = sorted(nums)
        l = res = 0

        for r, x in enumerate(nums):
            while x - nums[l] > 2 * k:
                l += 1
            res = max(res, r-l+1)

        return res