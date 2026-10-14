class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        res = [-1, -1]

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + ((r-l) // 2)

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                r = mid - 1
                res[0] = mid
        
        if res[0] == -1:
            return res
            
        l, r = res[0], len(nums) - 1

        while l <= r:
            mid = l + ((r-l) // 2)

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
                res[1] = mid
        
        return res