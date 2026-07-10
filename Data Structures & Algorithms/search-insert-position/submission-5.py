class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        last = 0

        while l <= r:
            m = l + ((r-l)//2)

            if nums[m] <= target:
                last = m
                l = m + 1
            else:
                r = m - 1

        print(last)

        if nums[last] == target:
            return last
        elif nums[last] < target:
            return last + 1
        else:
            return max(0, last - 1)