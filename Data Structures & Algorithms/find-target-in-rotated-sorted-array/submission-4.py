class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        l,r = 0,n-1
        while l<=r:
            # print(l,r,nums[l:r+1])
            mid = (l+r)//2
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            elif nums[mid] < target <= nums[r]:
                l = mid+1
            elif nums[mid] == target:
                return mid
            else:
                if nums[mid]>nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1
            