class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_len = 0
        for num in nums:
            if num-1 not in nums:
                i = num
                count = 1
                while i+1 in nums:
                    i += 1
                    count += 1
                max_len = max(max_len,count)
        
        return max_len
            