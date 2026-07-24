from collections import deque

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_mul = [1]
        postfix_mul = deque([1])

        for i in range(1, len(nums)):
            prefix_mul.append(nums[i-1] * prefix_mul[i-1])

        for i in range(len(nums)-2, -1, -1):
            postfix_mul.appendleft(nums[i+1] * postfix_mul[0])

        for i in range(len(nums)):
            prefix_mul[i] *= postfix_mul[i]
        
        return prefix_mul