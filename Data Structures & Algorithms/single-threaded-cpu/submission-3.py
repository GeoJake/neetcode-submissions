import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        output = []
        time = 0

        eHeap = [[tasks[i][0], tasks[i][1], i] for i in range(len(tasks))]
        processHeap = []

        eHeap.sort()
        i = 0

        while i < len(tasks) or processHeap:
            while i < len(tasks) and eHeap[i][0] <= time:
                val = eHeap[i]
                heapq.heappush(processHeap, (val[1], val[2]))
                i += 1
            
            if not processHeap and eHeap:
                time = eHeap[i][0]

            else:
                val = heapq.heappop(processHeap)
                time += val[0]
                output.append(val[1])
        return output