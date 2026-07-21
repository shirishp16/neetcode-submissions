class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        li, ri = 0, len(heights)-1
        while (li < ri):
            w = ri - li
            if heights[li] < heights[ri]:
                h = heights[li]
                li += 1
            else:
                h = heights[ri]
                ri -= 1
            curr = w*h
            if curr > maxArea:
                maxArea = curr
        
        return maxArea

            
