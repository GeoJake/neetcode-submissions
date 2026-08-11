class Solution:
    def reverse(self, x: int) -> int:
        
        flipped = 0
        negative = 1
        if x < 0:
            negative = -1
            x *= -1

        while x:
            flipped *= 10
            digit = x % 10
            x = x // 10
            flipped += digit
        
        maxInt = 1 << 31

        if negative == -1 and flipped < maxInt:
            return flipped * negative
        elif flipped < (maxInt - 1):
            return flipped
        else:
            return 0