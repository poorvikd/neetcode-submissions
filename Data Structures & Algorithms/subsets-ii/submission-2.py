class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        n = len(nums)
        nums.sort()
        def dfs(idx, subset):
            subsets.append(subset.copy())
            
            for i in range(idx,n):
                if i>idx and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                dfs(i+1, subset)
                subset.pop()

        dfs(0,[])
        return subsets
        