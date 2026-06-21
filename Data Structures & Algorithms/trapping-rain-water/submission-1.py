class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        if n == 1:
            return 0
        left_max = [0]*n
        right_max = [0]*n
        left_max[0] = height[0]
        right_max[-1] = height[-1]

        for i in range(1,n-1):
            left_max[i] = max(left_max[i-1],height[i])
            right_max[n-i-1] = max(right_max[n-i],height[n-i-1])
        
        left_max[n-1] = max(left_max[n-2],height[n-1])
        right_max[0] = max(right_max[1],height[0])

        vol = 0
        for i in range(n):
            vol += max(0,min(left_max[i],right_max[i])-height[i])
        return vol
        