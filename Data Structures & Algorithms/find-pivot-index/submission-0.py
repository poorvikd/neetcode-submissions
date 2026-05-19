class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = [0]
        for num in nums:
            prefixSum.append(prefixSum[-1]+num)

        for i in range(len(nums)):
            l_sum = prefixSum[i]
            r_sum = prefixSum[-1] - prefixSum[i+1]
            if l_sum == r_sum:
                return i
        return -1