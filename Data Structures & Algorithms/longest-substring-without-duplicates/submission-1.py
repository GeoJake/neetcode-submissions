class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        maxC = l = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.discard(s[l])
                l += 1
            seen.add(s[r])
            maxC = max(r-l+1, maxC)
        return maxC
            