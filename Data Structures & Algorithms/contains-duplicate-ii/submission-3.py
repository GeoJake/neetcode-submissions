class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dup = set()

        l = 0
        for r in range(len(nums)):
            if nums[r] in dup:
                return True
            
            if r-l >= k:
                dup.discard(nums[l])
                l += 1
            dup.add(nums[r])
        
        return False