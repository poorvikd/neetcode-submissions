class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        subsets = []
        nums.sort()
        n = len(nums)
        def dfs(idx, subsetSum, subset):
            if subsetSum == target:
                subsets.append(subset.copy())

            elif subsetSum > target:
                return
            
            for i in range(idx,n):
                subset.append(nums[i])
                dfs(i,subsetSum+nums[i],subset)
                subset.pop(-1)

        dfs(0,0,[])

        return subsets