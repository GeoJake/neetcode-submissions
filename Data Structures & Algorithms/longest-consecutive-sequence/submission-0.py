class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        conMap = {}
        minVal = float("-inf") 
        for n in nums:
            if n-1 in conMap:
                conMap[n-1] = n
            if not n in conMap:
                conMap[n] = float("-inf")
            if n+1 in conMap:
                conMap[n] = n + 1
            minVal = min(minVal, n)
        
        max_seq = 0

        for k in conMap.keys():
            seq = 0
            while k != float('-inf'):
                seq += 1
                k = conMap[k]

            max_seq = max(max_seq, seq)

        return max_seq