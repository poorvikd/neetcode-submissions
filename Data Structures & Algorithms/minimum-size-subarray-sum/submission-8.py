class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,0
        sm = nums[0]
        minlen = n + 1
        while l<=r and r<n:
            if sm >= target:
                minlen = min(minlen, r-l+1)
            if r == n-1:
                break
            r += 1
            sm += nums[r]
            while sm >= target:
                minlen = min(minlen, r-l+1)
                sm -= nums[l]
                l += 1
        
        return minlen if minlen != n+1 else 0

            


        