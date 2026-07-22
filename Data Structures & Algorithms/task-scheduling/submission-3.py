import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap = [-c for c in counts.values()]
        heapq.heapify(max_heap)
        
        queue = deque([])
        time = 0

        while max_heap or queue:
            time += 1
            if not max_heap:
                time = queue[0][1]
            else:
                c = 1 + heapq.heappop(max_heap)
                if c:
                    queue.append((c, time + n))
            
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])

        return time