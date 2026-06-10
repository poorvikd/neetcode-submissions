class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1:
            return math.ceil(piles[0]/h)
        max_rate = max(piles)
        # rates = [i for i in range(1,max_rate+1)]
    
        def time_taken(rate):
            time = 0
            for p in piles:
                time += math.ceil(p/rate)
            return time
    
        l,r = 1,max_rate
        min_rate = max_rate+1
        while l<=r:
            mid = (l+r)//2
            time = time_taken(mid)
            if time > h:
                l = mid+1
            else:
                r = mid-1
                min_rate = min(min_rate, mid)
        
        return min_rate

