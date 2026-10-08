class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}

        for s in strs:
            sortedStr = ''.join(sorted(s))
            if sortedStr in groups:
                groups[sortedStr].append(s)
            else:
                groups[sortedStr] = [s]
        
        res = []
        for k in groups.keys():
            res.append(groups[k])
        
        return res