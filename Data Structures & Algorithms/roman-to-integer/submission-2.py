class Solution:
    def romanToInt(self, s: str) -> int:
        
        res = 0
        i = 0

        romToInt = {"I": 1, "V": 5, "X": 10, 
                    "L": 50, "C": 100, "D": 500,
                    "M": 1000}

        while i < len(s):
            c = s[i]
            if i + 1 < len(s):
                c2 = s[i + 1]
                if c == "I":
                    if romToInt[c2] in [5, 10]:
                        res += (romToInt[c2] - romToInt[c])
                        i += 1
                    else:
                        res += romToInt[c]
                elif c == "X":
                    if romToInt[c2] in [50, 100]:
                        res += (romToInt[c2] - romToInt[c])
                        i += 1
                    else:
                        res += romToInt[c]

                elif c == "C":
                    if romToInt[c2] in [500, 1000]:
                        res += (romToInt[c2] - romToInt[c])
                        i += 1
                    else:
                        res += romToInt[c]
                else:
                    res += romToInt[c]
            else:
                res += romToInt[c]
            print(res)
            i += 1

        return res