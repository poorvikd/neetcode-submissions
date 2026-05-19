class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1

        while nums[l] > nums[r] and l<=r:
            mid = (l+r)//2
            # print(f"left:{nums[l]}, mid:{nums[mid]}, right:{nums[r]}")
            if nums[mid] > nums[r]:
                l = mid+1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                return nums[mid]
            
        return min(nums[l],nums[r])