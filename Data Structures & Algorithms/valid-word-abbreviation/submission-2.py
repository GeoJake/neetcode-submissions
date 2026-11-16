class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        w_p = a_p = 0

        while a_p < len(abbr):
            
            if abbr[a_p] <= 'z' and abbr[a_p] >= 'a':
                if w_p >= len(word) or not abbr[a_p] == word[w_p]:
                    return False
                a_p += 1
                w_p += 1
            else:
                if abbr[a_p] == '0':
                    return False
                number = 0
                while a_p < len(abbr) and abbr[a_p] >= '0' and abbr[a_p] <= '9':
                    number *= 10
                    number += int(abbr[a_p])
                    a_p += 1
                if w_p + number <= len(word):
                    w_p += number
                else:
                    return False
            
        return True