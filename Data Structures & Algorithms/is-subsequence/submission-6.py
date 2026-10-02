class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0

        for r in range(len(t)):
            if l >= len(s):
                return True
            
            if s[l] == t[r]:
                l += 1
        
        return l >= len(s)