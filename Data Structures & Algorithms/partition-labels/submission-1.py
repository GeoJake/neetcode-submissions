class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_seen = {}

        for i in range(len(s)):
            last_seen[s[i]] = i

        farthest = size = 0
        res = []
        
        for i, c in enumerate(s):
            farthest = max(farthest, last_seen[c])
            size += 1

            if i == farthest:
                res.append(size)
                size = 0
        
        return res