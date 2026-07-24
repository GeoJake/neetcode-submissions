from collections import deque

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p1 = p2 = 0

        len1 = len(nums1)
        len2 = len(nums2)

        combined_len = len1 + len2
        combined_mid = (combined_len // 2) + 1

        med1 = med2 = 0

        for idx in range(combined_mid):
            med2 = med1
            if p1 < len1 and p2 < len2:
                if nums1[p1] <= nums2[p2]:
                    med1 = nums1[p1]
                    p1 += 1
                    
                else:
                    med1 = nums2[p2]
                    p2 += 1
                
            elif p1 < len1:
                med1 = nums1[p1]
                p1 += 1
            else:
                med1 = nums2[p2]
                p2 += 1

        return med1 if combined_len % 2 else (med1 + med2) / 2
