class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)

        smallestLeftBar = [-1] * n
        smallestRightBar = [n] * n
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            while stack and h <= heights[stack[-1]]:
                stack.pop()
            if stack:
                smallestLeftBar[i] = stack[-1]
            stack.append(i)
        
        stack = []

        for i in range(n-1, -1, -1):
            h = heights[i]
            while stack and h <= heights[stack[-1]]:
                stack.pop()
            if stack:
                smallestRightBar[i] = stack[-1]
            stack.append(i)


        for i in range(n):

            maxArea = max(heights[i] * (smallestRightBar[i] - smallestLeftBar[i] - 1), maxArea)
        
        return maxArea