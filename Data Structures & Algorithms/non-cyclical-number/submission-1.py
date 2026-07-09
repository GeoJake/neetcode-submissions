class Solution:


    def isHappy(self, n: int) -> bool:
        seen = set()
    
        def helper(n):

            if n == 1:
                return True

            squaredTotal = 0
            while n:
                squaredTotal += (n % 10) ** 2
                n = n // 10
            
            if squaredTotal in seen:
                return False
            
            seen.add(squaredTotal)

            return helper(squaredTotal)

        return helper(n)