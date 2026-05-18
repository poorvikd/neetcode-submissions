class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        n = len(nums)
        visited = [0 for i in range(n)]
        def dfs(subset):
            if len(subset) == n:
                subsets.append(subset.copy())
            for i in range(0, n):
                if visited[i] == 0:
                    subset.append(nums[i])
                    visited[i] = 1
                    dfs(subset)
                    visited[i] = 0
                    subset.pop(-1)
            return

        dfs([])
        return subsets