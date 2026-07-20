import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x, y = heapq.heappop(stones), heapq.heappop(stones)
            diff = abs((-x) - (-y))
            if diff > 0:
                heapq.heappush(stones, -1 * diff)

        return 0 if len(stones) == 0 else -1 * stones[0]