class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        l = r = 0
        maxLen = 0

        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            maxLen = max(maxLen, len(s[l:r+1]))

            r += 1
        return maxLen
