class Solution:
    def isValid(self, s: str) -> bool:

        # Input: String contiaing only (), [], or {}
        # Output: Return True or False
        # Edge Cases: Odd char input Single closed or open parenthese, empty string, not a character listed above

        stack = []
        rel = {')': '(', '}': '{', ']': '['}

        if len(s) % 2:
            return False

        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if not len(stack) or not stack.pop() == rel[c]:
                    return False

        return len(stack) == 0
            