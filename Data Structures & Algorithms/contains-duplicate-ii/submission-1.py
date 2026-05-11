class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i,j = 0,1
        while i<j and j<len(nums):
            if nums[i] == nums[j]: return True
            elif j-i == k:
                i = i+1
                j = i+1
            else:
                j += 1
        return False
        
