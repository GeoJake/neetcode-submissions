class Solution:
    def trap(self, height: List[int]) -> int:
        maxA = 0

        l, r = 0, len(height)-1
        leftMax = height[l]
        rightMax = height[r]

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                maxA += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                maxA += rightMax - height[r]

        return maxA



            