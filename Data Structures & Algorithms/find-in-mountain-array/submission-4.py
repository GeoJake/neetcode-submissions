class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        res = -1
        length = mountainArr.length()

        l, r = 1, length - 2

        if length < 3:
            return res

        while l <= r:
            m = l + ((r-l) // 2)
            l_val = mountainArr.get(m-1)
            m_val = mountainArr.get(m)
            r_val = mountainArr.get(m+1)
            if l_val < m_val < r_val:
                l = m + 1         
            elif l_val > m_val > r_val:
                r = m - 1
            else:
                break
        
        peak = m

        low, high = 0, peak - 1

        while low <= high:
            middle = low + ((high-low) // 2)
            middle_val = mountainArr.get(middle)
            if middle_val < target:
                low = middle + 1
            elif middle_val > target:
                high = middle - 1
            else:
                return middle
        
        low, high = peak, length - 1
        
        while low <= high:
            middle = low + ((high-low) // 2)
            middle_val = mountainArr.get(middle)

            if target < middle_val:
                low = middle + 1
            
            elif target > middle_val:
                high = middle - 1
            
            else:
                return middle

        return -1