from collections import defaultdict, Counter
from operator import contains
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        n1,n2 = len(s), len(t)
        db1 = defaultdict(lambda: 0)
        db2 = Counter(t)
        res = [-1,-1]
        targetCount = len(db2)
        l = 0

        for r in range(n1):
            db1[s[r]] += 1
            if s[r] in db2 and db1[s[r]] == db2[s[r]]:
                targetCount -= 1
            
            while targetCount == 0:
                if res[0] == -1 or r-l < res[1]-res[0]:
                    res = [l,r]
                db1[s[l]] -= 1
                if s[l] in db2 and db1[s[l]] < db2[s[l]]:
                    targetCount += 1
                l += 1

        return s[res[0]:res[1]+1]