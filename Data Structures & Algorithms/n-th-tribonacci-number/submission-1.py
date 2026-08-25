class Solution:
    def tribonacci(self, n: int) -> int:

        arr = [-1] * (n + 1)
        
        def dfs(n: int) -> int:
            if arr[n] != -1:
                return arr[n]
            if n <= 1:
                return n
            if n == 2:
                return 1
            
            arr[n] = dfs(n-3) + dfs(n-2) + dfs(n-1)
            return arr[n]

        return dfs(n)