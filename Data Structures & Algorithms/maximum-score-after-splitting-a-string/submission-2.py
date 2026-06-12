class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        lz = [0 for i in range(n+1)]    
        ro = [0 for i in range(n+1)]

        for i in range(1,n+1):
            lz[i] = lz[i-1] + (1-int(s[i-1]))
            ro[n-i] = ro[n-i+1] + int(s[n-i])
        res = 0 
        for i in range(1,n):
            res = max(res,lz[i]+ro[i])
        return res
