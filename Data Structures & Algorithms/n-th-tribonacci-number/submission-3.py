class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        elif n == 2:
            return 1
        
        t0, t1, t2 = 0, 1, 1

        i = 3

        while i <= n:
            temp = t0 + t1 + t2
            t0 = t1
            t1 = t2
            t2 = temp
            i += 1

        return t2

                