class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftProd = [1 for i in range(n+1)]
        rightProd = [1 for i in range(n+1)]

        for i in range(n):
            leftProd[i+1] = leftProd[i]*nums[i]
        
        for i in range(n-1,-1,-1):
            rightProd[i] = rightProd[i+1]* nums[i]
        
        res = []
        for i in range(n):
            res.append(leftProd[i]*rightProd[i+1])

        return res