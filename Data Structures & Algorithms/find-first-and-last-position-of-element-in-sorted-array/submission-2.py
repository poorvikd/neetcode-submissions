class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l,r = 0,n-1
        l_pos = n+1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                l_pos = min(l_pos,mid)
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
        if l_pos == n+1:
            l_pos = -1
        r_pos = -1
        l,r = 0,n-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                r_pos = max(r_pos,mid)
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
        return [l_pos,r_pos]