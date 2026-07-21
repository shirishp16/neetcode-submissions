class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                if heights[i] < heights[j]:
                    h = heights[i]
                else:
                    h = heights[j]
                w = j - i
                curr = w*h
                if curr > maxArea:
                    maxArea = curr

        return maxArea
