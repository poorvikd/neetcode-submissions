class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals = sorted(intervals, key=lambda x:x[0])
        i = 0
        rem = 0
        while i<len(intervals)-1:
            l1,r1 = intervals[i]
            l2,r2 = intervals[i+1]
            if l2 < r1:
                if r2 > r1:
                    intervals.pop(i+1)
                elif r1 >= r2:
                    intervals.pop(i)
                rem += 1
            else:
                i += 1
        
        return rem
