class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0

        for i in range(len(heights)):
            minHeight = heights[i]
            area = 0
            for j in range(i, len(heights)):
                if heights[j] < minHeight:
                    minHeight = heights[j]
                area = minHeight * (1 + (j-i)) 
                if area > maxArea:
                    maxArea = area
        
        return maxArea