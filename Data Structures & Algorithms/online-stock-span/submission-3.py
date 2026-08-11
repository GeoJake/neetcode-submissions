class StockSpanner:

    def __init__(self):
        self.span = []

    def next(self, price: int) -> int:
        curr_span = 1

        while self.span and price >= self.span[-1][0]:
            curr_span += self.span[-1][1]
            self.span.pop()

        self.span.append((price, curr_span))

        return curr_span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)