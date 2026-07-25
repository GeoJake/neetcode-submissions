class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        conMap = defaultdict(int)
        max_seq = 0
        for n in nums:
            if not conMap[n]:
                conMap[n] = conMap[n-1] + conMap[n+1] + 1
                conMap[n - conMap[n - 1]] = conMap[n]
                conMap[n + conMap[n +1 ]] = conMap[n]
                max_seq = max(max_seq, conMap[n])

        return max_seq