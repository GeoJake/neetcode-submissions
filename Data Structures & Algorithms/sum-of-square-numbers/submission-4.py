import math 

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        l, r = 0, int(math.sqrt(c))
        
        x = int(math.sqrt(c // 2))

        if 2*(x**2) == c:
            return True

        while l <= r:
            total = l**2 + r**2
            if total > c:
                r -= 1
            elif total < c:
                l += 1
            else:
                return True
        
        return False