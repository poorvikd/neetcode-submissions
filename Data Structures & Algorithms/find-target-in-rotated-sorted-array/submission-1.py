class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l,r = 0,len(nums)-1

        while l<=r:
            mid = (l+r)//2
            print(f"l:{nums[l]} mid:{nums[mid]} r:{nums[r]}")
            if nums[l]<=target<nums[mid]:
                r = mid-1
            elif nums[mid]<target<=nums[r]:
                l = mid+1
            elif nums[mid] == target:
                return mid
            else:
                if nums[mid]>nums[r]:
                    l = mid+1
                else:
                    r = mid-1
                
        
        return -1
            