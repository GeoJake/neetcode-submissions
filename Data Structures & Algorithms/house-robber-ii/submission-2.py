class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = rob2 = 0
        rob3 = rob4 = 0

        for i in range(len(nums)):
            if i < len(nums) - 1:
                temp = max(nums[i] + rob1, rob2)
                rob1 = rob2
                rob2 = temp

            if i != 0:
                temp2 = max(nums[i] + rob3, rob4)
                rob3 = rob4
                rob4 = temp2

        return max(nums[0], rob2, rob4)

        