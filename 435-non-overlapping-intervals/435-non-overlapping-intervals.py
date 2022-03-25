class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        res = 0
        
        prevEnd = intervals[0][1]
        
        for start, end in intervals[1:]:
            # No overlap, change the new end
            if start >= prevEnd:
                prevEnd = end
            else:
                prevEnd = min(prevEnd, end)
                res += 1
        return res