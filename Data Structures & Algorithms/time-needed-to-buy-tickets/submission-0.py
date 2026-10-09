from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        q = deque([])

        for i, t in enumerate(tickets):
            q.append((i, t))

        time = 0
        while q:
            val = q.popleft()
            if val[0] == k and val[1] == 1:
                return time + 1
            elif val[1] > 1:
                q.append((val[0], val[1] - 1))
            time += 1
        
        return time