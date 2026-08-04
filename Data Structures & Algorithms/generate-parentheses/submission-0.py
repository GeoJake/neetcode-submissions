class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(subset, left, right):
            nonlocal n
            if left == right == n:
                res.append("".join(subset))
                return

            if left < n:
                subset.append('(')
                dfs(subset, left + 1, right)
                subset.pop()

            if right < left:
                subset.append(')')
                dfs(subset, left, right + 1)
                subset.pop()

        dfs([], 0, 0)

        return res