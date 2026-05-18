class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        subsets = set()
        candidates.sort()
        n = len(candidates)
        def dfs(idx, subsetSum, subset):
            if subsetSum == target:
                subsets.add(tuple(subset))

            elif subsetSum > target:
                return
            
            for i in range(idx,n):
                if i>idx and candidates[i] == candidates[i-1]:
                    continue
                subset.append(candidates[i])
                dfs(i+1,subsetSum+candidates[i],subset)
                subset.pop(-1)

        dfs(0,0,[])

        return list(map(list,subsets))