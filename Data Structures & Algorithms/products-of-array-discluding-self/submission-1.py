from collections import deque

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        postfix_mul = 1

        for i in range(1, len(nums)):
            res.append(nums[i-1] * res[i-1])

        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix_mul
            postfix_mul *= nums[i]
        
        return res