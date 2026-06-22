class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l,r = -1,-1
        sm = 0
        minlen = 1000000
        while l<=r and r<n-1:
            r += 1
            if l == -1:
                l = 0
            sm += nums[r]
            while sm >= target:
                minlen = min(minlen, r-l+1)
                sm -= nums[l]
                l += 1
        
        return minlen if minlen != 1000000 else 0

            


        