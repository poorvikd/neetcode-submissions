class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ps = [0 for i in range(n+1)]

        for i in range(1,n+1):
            ps[i] = nums[i-1] + ps[i-1]
        
        db = defaultdict(lambda: 0)
        db[0] = 1
        res = 0
        print(ps)
        for i in range(1,n+1):
            pair = ps[i] - k
            if db.get(pair, None):
                res += db[pair]
            db[ps[i]] += 1
        
        return res