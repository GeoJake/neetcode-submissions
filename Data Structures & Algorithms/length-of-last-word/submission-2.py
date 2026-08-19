class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while s[i] == " ":
            i -= 1
        
        firstChar = i

        while i > 0 and not s[i] == " ":
            i -= 1

        return 1 if i == firstChar else len(s[i:firstChar])