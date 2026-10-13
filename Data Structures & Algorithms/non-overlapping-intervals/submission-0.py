class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        #edge case
        if len(intervals)<=1:
            return 0
        intervals.sort(key = lambda x:x[0])
        count = 0
        res = [intervals[0]]
        for start,end in intervals[1:]:
            if start >= res[-1][1]:
                res.append([start,end])
            else:
                res[-1][1] = min(end,res[-1][1])
                count += 1
        return count
