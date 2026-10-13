class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if len(intervals) <= 1:
            return intervals
        
        intervals.sort(key=lambda x:x[0])

        res = [intervals[0]]

        for start,end in intervals[1:]:
            if start > res[-1][1]:
                res.append([start,end])
            else:
                res[-1][1] = max(end,res[-1][1])
        return res