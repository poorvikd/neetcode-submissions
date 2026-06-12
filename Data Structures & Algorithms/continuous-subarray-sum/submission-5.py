class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        ps = [0 for i in range(n+1)]
        db = defaultdict()
        db[0] = 0

        for i in range(1,n+1):
            ps[i] = ps[i-1] + nums[i-1]
            rem = ps[i] % k 
            if rem in db:
                if (i-db[rem]) >= 2:
                    return True
            else:
                db[rem] = i
        
        return False
