class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""
        
        t_chars = {}

        missing_chars = 0

        for c in t:
            if not c in t_chars:
                t_chars[c] = 0
            t_chars[c] += 1
            missing_chars += 1
        
        res = ""

        l = r = 0

        while r < len(s):

            if s[l] not in t_chars:
                l += 1
            
            if s[r] in t_chars:
                if t_chars[s[r]] > 0:
                    missing_chars -= 1
                t_chars[s[r]] -= 1

            while not missing_chars and l <= r:
                newStr = s[l:r+1]

                if res == "":
                    res = newStr
                else:
                    if len(s[l:r+1]) < len(res):
                        res = newStr

                if s[l] in t_chars:
                    char_amt = t_chars[s[l]]
                    
                    if char_amt >= 0:
                        missing_chars += 1
                    t_chars[s[l]] += 1
                    
                l += 1

            r += 1
        
        return res