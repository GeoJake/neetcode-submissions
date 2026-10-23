class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        k %= n
        start = swaps = 0

        while swaps < n:
            current = start
            prev = nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                swaps += 1
                if start == current:
                    break
            start += 1
            

        # 1, 2, 3, 4, 5 
        # 5, 1, 2, 3, 4, 

        # (0 + 6) % 5 = 1

        # 1, 2, 3, 4, 5, 6
        # 4, -, 6, 1, -, 3

        # (0 - 1) % 5

        # 1, 2, 3, 4, 5, 6, 7
        # -, -, -, 1, -, -, 4