class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        ## Insertion Sort
        # for i in range(1,len(nums)):
        #     j = i-1
        #     while j>=0 and nums[j]>nums[j+1]:
        #         nums[j],nums[j+1] = nums[j+1],nums[j]
        #         j -= 1
        
        ## Selection Sort
        n = len(nums)
        for i in range(n):
            mn = nums[i]
            mn_i = i
            for j in range(i+1,n):
                if mn>nums[j]:
                    mn_i = j
                    mn = nums[j]
            nums[i],nums[mn_i] = nums[mn_i],nums[i]
            
        return nums
                