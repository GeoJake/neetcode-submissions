class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x

        last = 0

        while l <= r:
            m = l + ((r-l)//2)

            if m ** 2 <= x:
                last = m
                l = m + 1
            else:
                r = m - 1
        
        return last