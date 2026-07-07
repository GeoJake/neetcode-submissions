class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        speed = 0

        while l <= r:
            mid_speed = l + ((r-l)//2)
            total_hours = 0
            for p in piles:
                total_hours += math.ceil(p/mid_speed)

            if total_hours <= h:
                speed = mid_speed
                r = mid_speed-1
            else:
                l = mid_speed+1
        
        return speed