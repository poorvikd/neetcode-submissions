"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        if n == 0:
            return 0
        if n == 1:
            return 1

        intervals = sorted(intervals, key=lambda x:x.start)
        rooms = [0]
        heapq.heapify(rooms)
        for i in intervals:
            s,e = i.start, i.end
            room_avail = rooms[0]
            if room_avail <= s:
                heapq.heappop(rooms)
                heapq.heappush(rooms,e)
            else:
                heapq.heappush(rooms,e)
        return len(rooms)
            

