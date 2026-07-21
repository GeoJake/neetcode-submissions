import heapq
import math
class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for p in points:
            d = -(p[0]**2 + p[1]**2)
            heapq.heappush(heap, (d, p))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []

        while heap:
            d, p = heapq.heappop(heap)
            res.append([p[0], p[1]])
        
        return res