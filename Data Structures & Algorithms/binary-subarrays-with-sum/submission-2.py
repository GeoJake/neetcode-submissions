class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        def helper(x: int) -> int:
            if x < 0:
                return 0

            l = sumVals = count = 0
            for r in range(len(nums)):
                sumVals += nums[r]
                while sumVals > x:
                    sumVals -= nums[l]
                    l += 1
                count += r - l + 1
            
            return count

        return helper(goal) - helper(goal - 1)