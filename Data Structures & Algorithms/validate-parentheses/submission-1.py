class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        rel = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:

                if not len(stack) or not stack.pop() == rel[c]:
                    return False

        return len(stack) == 0
            