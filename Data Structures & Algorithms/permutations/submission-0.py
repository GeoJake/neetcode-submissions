class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        freq = Counter(nums)

        def findPerms(subset):
            if len(subset) == len(nums):
                out.append(subset.copy())
                return

            for n in freq.keys():
                if freq[n]:
                    subset.append(n)
                    freq[n] -= 1
                    findPerms(subset)
                    subset.pop()
                    freq[n] += 1
        
        findPerms([])

        return out
