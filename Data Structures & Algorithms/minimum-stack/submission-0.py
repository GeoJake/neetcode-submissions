class MinStack:

    def __init__(self):
        self.min = []
        self.stack = []

    def push(self, val: int) -> None:
        if not self.min:
            self.min.append(val)
        else:
            if val < self.min[-1]:
                self.min.append(val)
            else:
                self.min.append(self.min[-1])
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
