class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        while count < len(nums):
            if not count == nums[count]:
                return count
            count += 1
        
        return count