class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0

        while r < len(nums):
            count = 1

            while r + 1 < len(nums) and nums[r] == nums[r+1]:
                r += 1
                count += 1

            amt_of_val = min(2, count)
            for i in range(amt_of_val):
                nums[l] = nums[r]
                l += 1
            r += 1
        return l
                    

        

        