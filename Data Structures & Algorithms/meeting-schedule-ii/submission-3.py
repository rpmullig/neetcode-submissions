"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: (x.start, x.end))
        h = []
        max_rooms = 0
        for interval in intervals:
            while len(h) > 0 and h[0] <= interval.start:
                heapq.heappop(h)

            heapq.heappush(h, interval.end)
            max_rooms = max(max_rooms, len(h))

        return max_rooms