class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        l,r = 0,n-1
        while l<r:
            area = (r-l)*min(heights[r],heights[l])
            maxArea = max(area,maxArea)
            if heights[r]>heights[l]:
                l += 1
            else:
                r -= 1

            
        return maxArea
