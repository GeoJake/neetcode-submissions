class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"

        for i in range(1, n):
            rs = ""
            for j in range(len(s)-1, -1, -1):
                c = s[j]
                if c == "0":
                    rs += "1"
                else:
                    rs += "0" 
            s += "1"
            s += rs

        return s[k-1]