class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for n in nums:
            seen.add(n)
            
        return not len(seen) == len(nums)