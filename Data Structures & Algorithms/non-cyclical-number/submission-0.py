class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        squaredTotal = 0

        while squaredTotal != 1 and n != 1:
            print(seen)
            while n:
                squaredTotal += (n % 10) ** 2
                n = n // 10
            
            if squaredTotal in seen:
                return False
            
            n = squaredTotal
            seen.add(squaredTotal)
            squaredTotal = 0
        
        return True