class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        min_heap = [(0, 0, 0)] #effort, row, col
        d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        seen = set()
        ROWS, COLS = len(heights), len(heights[0])

        while min_heap:
            diff, r, c = heapq.heappop(min_heap)

            if (r, c) in seen:
                continue
            
            seen.add((r, c))

            if (r, c) == (ROWS-1, COLS-1):
                return diff
            
            for dr, dc in d:
                newR, newC = r + dr, c + dc
                if (
                    newR < 0 or newC < 0 or
                    newR >= ROWS or newC >= COLS or
                    (newR, newC) in seen
                ):
                    continue
                
                newDiff = max(diff, abs(heights[r][c] - heights[newR][newC]))
                heapq.heappush(min_heap, (newDiff, newR, newC))

        return 0