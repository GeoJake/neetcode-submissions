class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_seen = {}

        for i in range(len(s)):
            last_seen[s[i]] = i

        farthest = last_seen[s[0]]
        split = 0
        res = []
        
        for i in range(len(s)):
            farthest = max(farthest, last_seen[s[i]])
            if i == farthest:
                res.append(len(s[split : i+1]))
                split = i + 1
        
        return res