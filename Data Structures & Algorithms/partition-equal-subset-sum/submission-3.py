class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2:
            return False
        
        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for n in nums:
            for j in range(len(dp)-1, n-1, -1):
                dp[j] = dp[j] | dp[j - n]
        
        return dp[target]