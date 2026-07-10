class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        prefix_zeros = [0]
        for n in nums:
            if n:
                prefix_zeros.append(prefix_zeros[-1])
            else:
                prefix_zeros.append(prefix_zeros[-1] + 1)
        print(prefix_zeros)

        out = 0
        for low in range(len(nums)):
            l, r = low, len(nums)
            while l < r:
                m = l + ((r-l)//2)

                if prefix_zeros[m+1] - prefix_zeros[low] <= k:
                    l = m + 1
                else:
                    r = m
                
                out = max(out, l - low)

        return out