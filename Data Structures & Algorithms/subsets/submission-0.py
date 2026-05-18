class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = set()
        n = len(nums)
        def dfs(idx, subset):
            # subset.append(nums[idx])
            if tuple(subset) not in subsets:
                subsets.add(tuple(subset))
            for i in range(idx, n):
                subset.append(nums[i])
                dfs(i+1,subset)
                subset.pop(-1)
            return

        dfs(0,[])
        return list(map(list,subsets))