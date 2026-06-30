class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        l = maxC = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.discard(s[l])
                l += 1
            maxC = max(maxC, r - l + 1)
            seen.add(s[r])
            r += 1
        
        return maxC