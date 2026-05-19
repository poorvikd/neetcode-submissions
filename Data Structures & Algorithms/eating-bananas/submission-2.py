class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1:
            return math.ceil(piles[0]/h)
        maxPile = max(piles)

        # rates = [i for i in range(1,maxPile+1)]

        def timeCalc(k):
            time = 0
            for p in piles:
                time += math.ceil(p/k)
            return time
        
        l,r = 1, maxPile
        min_k = maxPile+1
        while l<=r:
            mid = (l+r)//2
            time = timeCalc(mid)
            if time <= h:
                min_k = min(min_k,mid)
                r = mid-1
            else:
                l = mid+1
        
        return min_k