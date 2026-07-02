class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        distinct_chars = set(s)

        longestRepStr = 0
        replacements = 0

        for c in distinct_chars:
            left = count = 0
            for right in range(len(s)):
                if s[right] == c:
                    count += 1
                
                while (right-left+1) - count > k:
                    if s[left] == c:
                        count -= 1
                    left += 1
                
                longestRepStr = max(longestRepStr, right-left+1)
        
        return longestRepStr
