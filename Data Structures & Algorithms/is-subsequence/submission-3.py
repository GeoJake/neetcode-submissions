class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1 = p2 = 0

        if s == "":
            return True

        while p1 < len(s) and p2 < len(t):
            if s[p1] == t[p2]:
                if p1 == len(s)-1:
                    return True
                else:
                    p1 += 1
                    p2 += 1
            else:
                p2 += 1
        
        return False