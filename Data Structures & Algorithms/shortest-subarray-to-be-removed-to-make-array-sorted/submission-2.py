class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        n = len(arr)
        
        r = n - 1

        while r > 0 and arr[r - 1] <= arr[r]:
            r -= 1
        
        if not r:
            return 0
        
        res = r

        for l in range(n):
            if l > 0 and arr[l - 1] > arr[l]:
                break
            while r < n and arr[r] < arr[l]:
                r += 1
            res = min(res, r - l - 1)

        return res