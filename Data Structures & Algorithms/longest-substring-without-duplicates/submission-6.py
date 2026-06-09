class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0 or n==1:
            return n
        l,r = 0,0
        db = {}
        db[s[r]] = 1
        maxLen = 1
        while l<=r and r<n:
            if r == n-1:
                break
            if s[r+1] in db:
                while s[r+1] in db:
                    del db[s[l]]
                    l += 1
            r += 1
            db[s[r]] = 1
            maxLen = max(maxLen,r-l+1)

        return maxLen            


