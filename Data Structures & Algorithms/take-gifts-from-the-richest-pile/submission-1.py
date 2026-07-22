import heapq
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxHeap = [-x for x in gifts]
        heapq.heapify(maxHeap)

        while k:
            val = math.floor(math.sqrt(-heapq.heappop(maxHeap)))
            heapq.heappush(maxHeap, -val)
            k -= 1
        
        return -sum(maxHeap)