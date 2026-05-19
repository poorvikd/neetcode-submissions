class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefixArr = [0]
        for num in nums:
            self.prefixArr.append(self.prefixArr[-1]+num)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixArr[right+1] - self.prefixArr[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)