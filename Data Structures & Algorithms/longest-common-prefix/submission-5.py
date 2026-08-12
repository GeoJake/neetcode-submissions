class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        word = strs[0]
        for i in range(len(word)):
            for s in strs:
                if len(s) == i or not word[i] == s[i]:
                    return word[:i]
        
        return word