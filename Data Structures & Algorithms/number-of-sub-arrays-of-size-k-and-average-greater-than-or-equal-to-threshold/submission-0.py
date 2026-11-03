class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        total = 0

        for i in range(k):
            total += arr[i]

        avg = total / k

        res = 0

        if avg >= threshold:
            res += 1

        for i in range(k, len(arr)):
            total += arr[i]
            total -= arr[i-k]
            avg = total / k

            if avg >= threshold:
                res += 1
        
        return res
            
