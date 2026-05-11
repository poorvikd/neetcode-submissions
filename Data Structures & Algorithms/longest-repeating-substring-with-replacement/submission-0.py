class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l,r = 0,0
        db = defaultdict(lambda:0)
        db[s[l]] = 1
        maxWindow = 0
        while l<=r and r<n-1:
            r += 1
            db[s[r]] += 1
            maxFreq = max(db.values())
            windowLen = r - l + 1
            while windowLen - maxFreq > k:
                db[s[l]] -= 1
                if db[s[l]] == 0:
                    del db[s[l]]
                l += 1 
                windowLen -= 1
                maxFreq = max(db.values())    
            maxWindow = max(maxWindow,r-l+1)
        return maxWindow

