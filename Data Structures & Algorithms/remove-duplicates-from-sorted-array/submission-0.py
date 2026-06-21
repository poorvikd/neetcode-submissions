class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        nxt = 1
        k = 1
        for i in range(1,n):
            if nums[i] == nums[i-1]:
                continue
            else:
                nums[nxt] = nums[i]
                k += 1
                nxt += 1
        
        return k

