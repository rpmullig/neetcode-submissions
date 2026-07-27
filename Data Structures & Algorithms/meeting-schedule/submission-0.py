"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: (x.start, x.end))
        end_of_current_meeting = None
        for interval in intervals:
            if not end_of_current_meeting:
                start, stop = interval.start, interval.end
                end_of_current_meeting = stop
                continue
            else:
                start, stop = interval.start, interval.end
                if start < end_of_current_meeting:
                    return False
                else:
                    end_of_current_meeting = stop
        
        return True