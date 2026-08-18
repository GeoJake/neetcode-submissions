class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "+":
                total = stack[-1] + stack[-2]
                stack.append(total)
            elif op == "C" and stack:
                stack.pop()
            elif op == "D" and stack:
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(op))

        return sum(stack)