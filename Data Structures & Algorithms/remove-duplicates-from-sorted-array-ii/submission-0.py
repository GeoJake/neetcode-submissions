class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        count = Counter(nums)
        i = 0
        for num in count:
            nums[i] = num
            count[num] -= 1
            i += 1
            if count[num] >= 1:
                nums[i] = num
                i += 1
        return i

        

        