class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        n = len(nums)
        i,j = 0,1
        db = {}
        db[nums[i]] = 1
        while i<j and j<n:
            if db.get(nums[j],None) != None and abs(j-i) <= k:
                return True
            elif abs(j-i)<=k:
                db[nums[j]] = 1
                j += 1
            else:
                db[nums[i]] -= 1
                if db[nums[i]] == 0:
                    del db[nums[i]]
                i += 1
        
        return False
            

        