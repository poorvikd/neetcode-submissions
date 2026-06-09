class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        minLength = n+1
        l,r = 0,0
        arr_sum = nums[r]

        while l<=r and r<n:
            if arr_sum >= target:
                minLength = min(minLength,r-l+1)
            if r==n-1:
                break
            r += 1
            arr_sum += nums[r]
            while l<=r and arr_sum >= target:
                minLength = min(minLength,r-l+1)
                arr_sum -= nums[l]
                l += 1
            
        if minLength > n:
            return 0
        return minLength