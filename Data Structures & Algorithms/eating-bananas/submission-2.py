class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        speed = 0

        while l <= r:
            mid = l + ((r-l)//2)
            hours = sum([math.ceil(pile/mid) for pile in piles])

            if hours <= h:
                speed = mid
                r = mid-1
            else:
                l = mid+1
        
        return speed