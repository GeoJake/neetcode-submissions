class StockSpanner:

    def __init__(self):
        self.span = []

    def next(self, price: int) -> int:
        if not self.span:
            self.span.append((price, 1))
            return 1

        p = len(self.span) - 1
        curr_span = 1

        while p >= 0 and price >= self.span[p][0]:
            curr_span += self.span[p][1]
            p -= self.span[p][1]

        self.span.append((price, curr_span))

        return curr_span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)