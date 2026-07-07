class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        min_num = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                return min(min_num, nums[l])
            
            mid = l + ((r-l)//2)
            min_num = min(min_num, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        
        return min_num