class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #edge case
        if not intervals:
            return [newInterval]
        #find the first start smaller than the previous one
        i = 0
        while i < len(intervals) and intervals[i][0] < newInterval[0]:
            i += 1
        intervals.insert(i,newInterval)

        result = [intervals[0]]
        for start, end in intervals[1:]:
            if start > result[-1][1]:
                result.append([start,end])
            else:
                result[-1][1] = max(end,result[-1][1])
        return result


        