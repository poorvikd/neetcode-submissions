class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        n = len(nums)
        def dfs(subset):
            if len(subset) == n:
                subsets.append(subset.copy())
            for i in range(0, n):
                if nums[i] not in subset:
                    subset.append(nums[i])
                    dfs(subset)
                    subset.pop(-1)
            return

        dfs([])
        return subsets