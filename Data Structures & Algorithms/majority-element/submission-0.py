class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)

        for i in freq.keys():
            if freq[i] > len(nums)/2:
                return i
        