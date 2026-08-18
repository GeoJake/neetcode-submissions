class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0

        for op in operations:
            if op == "+":
                total = stack[-1] + stack[-2]
                stack.append(total)
                res += total
            elif op == "C" and stack:
                val = stack.pop()
                res -= val
            elif op == "D" and stack:
                stack.append(stack[-1] * 2)
                res += stack[-1]
            else:
                stack.append(int(op))
                res += int(op)

        return res