class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        db = defaultdict(lambda:0)
        db[s[r]] = 1
        n = len(s)
        maxLen = 1
        max_freq = 1
        while r < n-1:
            r = r+1
            db[s[r]] += 1
            # max_freq = max(db.values())
            max_freq = max(max_freq, db[s[r]])
            if (r-l+1) - max_freq > k:
                db[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r-l+1)
        
        return maxLen
