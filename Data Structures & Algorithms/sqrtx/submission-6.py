class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        l,r = 1,x//2
        res = 1
        while l<=r:
            mid = (l+r)//2
            if mid*mid > x:
                r = mid - 1
            elif mid*mid < x:
                res = mid
                l = mid+1
            else:
                return mid
        return res
        
