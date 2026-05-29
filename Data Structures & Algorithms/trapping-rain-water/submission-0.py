class Solution:
    def trap(self, height: List[int]) -> int:
        maxA = 0
        n = len(height)

        if not n:
            return maxA

        for i in range(n):
            
            leftMax = rightMax = height[i]

            for j in range(i):
                if height[j] > leftMax:
                    leftMax = height[j]
            
            for k in range(i+1, n):
                if height[k] > rightMax:
                    rightMax = height[k]
            
            maxA += min(leftMax, rightMax) - height[i]

        return maxA



            