import heapq

class MedianFinder:

    def __init__(self):
        self.l_h = []
        self.r_h = []

    def addNum(self, num: int) -> None:
        l_size = len(self.l_h)
        r_size = len(self.r_h)

        if l_size == r_size:
            if not self.r_h or num < self.r_h[0]:
                heapq.heappush(self.l_h, -num)
            else:
                heapq.heappush(self.l_h, -heapq.heappop(self.r_h))
                heapq.heappush(self.r_h, num)
        else:
            if num > -self.l_h[0]:
                heapq.heappush(self.r_h, num)
            else:
                heapq.heappush(self.r_h, -heapq.heappop(self.l_h))
                heapq.heappush(self.l_h, -num)

    def findMedian(self) -> float:
        total_len = len(self.l_h) + len(self.r_h)
        if total_len % 2:
            return -self.l_h[0]
        else:
            return (-self.l_h[0] + self.r_h[0])/2