class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = set()
        n = len(nums)
        nums.sort()
        def dfs(idx, subset):
            if tuple(subset) not in subsets:
                subsets.add(tuple(subset))
            
            for i in range(idx,n):
                if i>idx and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                dfs(i+1, subset)
                subset.pop(-1)

        dfs(0,[])
        return list(map(list,subsets))
        