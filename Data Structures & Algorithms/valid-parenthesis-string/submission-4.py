class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        starStack = []

        for i, c in enumerate(s):
            if c == '(':
                stack.append(['(', i])
            elif c == '*':
                starStack.append(['*', i])
            elif c == ')':
                if stack and stack[-1][0] == '(':
                    stack.pop()
                elif starStack and starStack[-1][0] == '*':
                    starStack.pop()
                else:
                    return False

        while stack and starStack:
            if stack.pop()[1] > starStack.pop()[1]:
                return False
        
        return not stack