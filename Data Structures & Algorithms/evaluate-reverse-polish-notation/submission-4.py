class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        total = 0
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "-":
                v1, v2 = stack.pop(), stack.pop()
                stack.append(v2 - v1)
            elif i == "/":
                v1, v2 = stack.pop(), stack.pop()
                stack.append(int(float(v2) / v1))
            else:
                stack.append(int(i))
        
        return stack[0]