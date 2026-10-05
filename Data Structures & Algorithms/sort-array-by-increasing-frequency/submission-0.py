class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = {}

        max_count = 0

        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1
        
        nums.sort(key=lambda n:(count[n], -n))
        return nums