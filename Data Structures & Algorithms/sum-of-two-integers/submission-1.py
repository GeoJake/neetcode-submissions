class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0
        
        print(a.bit_length())
        print(b.bit_length())

        for i in range(32):
            pos = 1 << i
            oneA = (a & pos)
            oneB = (b & pos)

            if (carry and oneA and oneB):
                res |= pos
                carry = 1
            elif (carry and (oneA or oneB)) or (oneA and oneB):
                res |= (0 << i)
                carry = 1
            elif oneA or oneB or carry:
                res |= pos
                carry = 0
            else:
                carry = 0

        if res > 0x7FFFFFFF:
            res = ~(res ^ 0xFFFFFFFF)    
        
        return res