import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [[x, i] for i, x in enumerate(nums)]
        heapq.heapify(heap)

        for _ in range(k):
            minVal = heapq.heappop(heap)
            minVal[0] = minVal[0] * multiplier 
            nums[minVal[1]] = minVal[0]
            heapq.heappush(heap, minVal)
        
        return nums