class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = [0]
        for num in nums:
            prefixSum.append(prefixSum[-1]+num)
        
        db = defaultdict(lambda:0)
        # db[0] = 1
        res = 0
        for i in range(len(prefixSum)):
            if prefixSum[i] - k in db:
                res += db[prefixSum[i]-k]
            db[prefixSum[i]] += 1
        
        return res