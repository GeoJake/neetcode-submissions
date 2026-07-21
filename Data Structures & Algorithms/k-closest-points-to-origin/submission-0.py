import heapq
import math
class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for p in points:
            heap.append((-1*math.sqrt((p[0])**2 + (p[1])**2), p))

        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)
        
        return [x[1] for x in heap]