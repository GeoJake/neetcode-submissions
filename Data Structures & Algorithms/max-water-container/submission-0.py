class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxA = 0
        
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                area = (j-i) * min(heights[i], heights[j])
                if maxA < area:
                    maxA = area
        
        return maxA