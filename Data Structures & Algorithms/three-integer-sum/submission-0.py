class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        for i in range(n-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1,n-1
            target = -nums[i]
            db = defaultdict(list)
            for j in range(l,r+1):
                if target - nums[j] in db:
                    sol = [nums[i],nums[j],target - nums[j]]
                    sol.sort()
                    if sol not in res:
                        res.append(sol)
                else:
                    db[nums[j]].append(j)

        
        return res
        
