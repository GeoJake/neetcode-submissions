class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        flipped = 0

        while n > 1:
            middle = 1 << (n-1)
            if k == middle:
                return str(1 ^ flipped)
            if k > middle:
                k = 2 * middle - k
                flipped ^= 1
            n -= 1
        
        return str(flipped)