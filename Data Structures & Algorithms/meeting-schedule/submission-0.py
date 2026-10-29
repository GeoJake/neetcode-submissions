"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        def order(a: Interval) -> int:
            return a.end
        
        intervals.sort(key=order)

        prev_end = 0
        for i in intervals:
            start = i.start
            end = i.end
            if start < prev_end:
                return False
            else:
                prev_end = end

        return True