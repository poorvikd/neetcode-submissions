from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        l,r = 0,0
        db1 = Counter(s1)
        db2 = {}
        while l<=r and r<n2:
            if r-l+1 <= n1:
                if s2[r] in db1 and db1[s2[r]] > db2.get(s2[r],0):
                    db2[s2[r]] = db2.get(s2[r],0) + 1
                    r += 1
                else:
                    l += 1
                    r = l
                    db2 = {}
            else:
                return True
        if r-l == n1:
            return True
        return False





        
        

        

        
            
