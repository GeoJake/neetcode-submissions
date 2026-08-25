class Solution:
    def tribonacci(self, n: int) -> int:

        arr = [-1] * (n + 1)
        
        # def dfs(n: int) -> int:
        #     if arr[n] != -1:
        #         return arr[n]
        #     if n <= 1:
        #         return n
        #     if n == 2:
        #         return 1
            
        #     arr[n] = dfs(n-3) + dfs(n-2) + dfs(n-1)
        #     return arr[n]

        i = 0

        while i <= n:
            if i <= 1:
                arr[i] = i
            elif i == 2:
                arr[i] = 1
            else:
                arr[i] = arr[i-3] + arr[i-2] + arr[i-1]
            i += 1
        return arr[n]

                