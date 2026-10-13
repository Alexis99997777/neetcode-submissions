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
        #edge case
        if len(intervals) <= 1:
            return len(intervals)
        intervals.sort(key = lambda x:x.start)
        heap = []
        n = len(intervals)
        #store end time
        for i in range(n):
            if heap and heap[0] <= intervals[i].start:
                heapq.heappop(heap)
            heapq.heappush(heap,intervals[i].end)
        return len(heap)
        