class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        freq = defaultdict(int)

        for i in nums:
            freq[i] += 1

        res = []

        for i in range(len(nums)):
            freq[nums[i]] -= 1
            if i and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums)):
                freq[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j-1]:
                    continue

                target = -(nums[i] + nums[j])
                if freq[target] > 0:
                    res.append([nums[i], nums[j], target])
            
            for j in range(i+1, len(nums)):
                freq[nums[j]] += 1

        return res