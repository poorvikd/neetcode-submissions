class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_weight = sum(weights)

        def calc_days(weight):
            sm = 0
            days = 1
            for w in weights:
                if sm + w <= weight:
                    sm += w
                else:
                    days += 1
                    sm = w
            return days
        
        l,r = max(weights), max_weight
        res = max_weight+1
        while l<=r:
            mid = (l+r)//2
            num_days = calc_days(mid)
            if num_days > days:
                l = mid+1
            elif num_days <= days:
                res = min(res, mid)
                r = mid-1
        
        return res

