class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        n = len(nums)
        l,r = 0, n-1
        min_val = 10000
        while l <= r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                min_val = min(min_val, nums[mid])
                r = mid - 1
        
        return min_val
                
