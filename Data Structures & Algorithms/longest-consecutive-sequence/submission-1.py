class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = set(nums)

        start = {}

        for num in nums:
            if num-1 not in nums:
                start[num] = 1
        max_len = -1
        for num in start.keys():
            i = num
            while i+1 in nums:
                start[num] += 1
                i += 1
            max_len = max(max_len,start[num])
        
        return max_len
            