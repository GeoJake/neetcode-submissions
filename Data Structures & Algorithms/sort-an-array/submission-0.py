class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = (len(nums) // 2) - 1

        for i in range(n, -1, -1):
            self.heapify(nums, len(nums), i)

        heap_size = len(nums)

        while heap_size > 1:
            nums[0], nums[heap_size-1] = nums[heap_size-1], nums[0]
            heap_size -= 1
            self.heapify(nums, heap_size, 0)

        return nums
    
    def heapify(self, nums: List[int], n: int, i: int):
        if i >= n:
            return

        l = 2*i + 1
        r = 2*i + 2

        largest = i

        if l < n and nums[l] > nums[largest]:
            largest = l
        
        if r < n and nums[r] > nums[largest]:
            largest = r
        
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            self.heapify(nums, n, largest)
