class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        ## Insertion Sort
        for i in range(1,len(nums)):
            j = i-1
            while j>=0 and nums[j]>nums[i]:
                nums[i],nums[j] = nums[j],nums[i]
                i -= 1
                j -= 1
        
        return nums
                