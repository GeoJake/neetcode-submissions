from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = r = 0

        win_max = deque()

        while r < len(nums):
            while win_max and nums[win_max[-1]] < nums[r]:
                win_max.pop()
            win_max.append(r)

            if l > win_max[0]:
                win_max.popleft()
            
            if (r + 1) >= k:
                res.append(nums[win_max[0]])
                l += 1
            r += 1
        
        return res