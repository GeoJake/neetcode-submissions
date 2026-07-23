import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []

        for f in freq:
            heapq.heappush(heap, (freq[f], f))
            while len(heap) > k:
                heapq.heappop(heap)
            
        return [h[1] for h in heap]