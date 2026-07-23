import heapq
class Solution:
    
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        heap = []
        people = 0
        for numPass, start, end in trips:
            while heap and heap[0][0] <= start:
                people -= heapq.heappop(heap)[1]
            people += numPass
            if people > capacity:
                return False
            heapq.heappush(heap, (end, numPass))

        return True