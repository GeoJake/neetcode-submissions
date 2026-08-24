class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        maxCount = 0
        count = 0
        for i in range(len(nums)):
            if nums[i]:
                count += 1
            else:
                count = 0
            
            maxCount = max(maxCount, count)
        
        return maxCount