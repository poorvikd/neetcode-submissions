class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        db = defaultdict(item=0)
        l,r = 0,0
        db[s[l]] = 1
        maxWindow = 1
        while l<=r and r<len(s)-1:
            if db.get(s[r+1],None) == None:
                r += 1
                db[s[r]] = 1
                print(maxWindow,s[l:r+1])
                maxWindow = max(maxWindow,r-l+1)
            else:
                while s[l] != s[r+1]:
                    del db[s[l]]
                    l += 1
                l += 1
                r += 1

        return maxWindow

