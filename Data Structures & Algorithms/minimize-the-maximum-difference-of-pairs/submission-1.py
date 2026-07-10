class Solution:

    

    def minimizeMax(self, nums: List[int], p: int) -> int:
        if not p:
            return 0
        
        nums.sort()

        def isValid(t: int):

            i = count = 0

            while i < len(nums)-1:
                if nums[i+1] - nums[i] <= t:
                    count += 1
                    i += 2
                else:
                    i += 1
            
                if count == p:
                    return True

            return False

        l, r = 0, nums[-1] - nums[0]

        thresh = nums[-1] - nums[0]

        while l <= r:
            m = l + ((r-l)//2)
            if isValid(m):
                thresh = m
                r = m - 1
            else:
                l = m + 1
        
        return thresh

