import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        output = []
        nextI = 0

        eHeap = [[tasks[i][0], tasks[i][1], i] for i in range(len(tasks))]
        processHeap = []

        heapq.heapify(eHeap)
        time = 0

        while eHeap or processHeap:
            while eHeap and eHeap[0][0] <= time:
                val = heapq.heappop(eHeap)
                heapq.heappush(processHeap, (val[1], val[2]))
            
            if not processHeap and eHeap:
                time = eHeap[0][0]

            else:
                val = heapq.heappop(processHeap)
                time += val[0]
                output.append(val[1])
        
        return output