from collections import deque
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        changes = 0
        nextVal = 0
        for n in sorted(nums):
            chosen = max(n, nextVal)
            changes += chosen - n
            nextVal = chosen + 1
        return changes