class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: (x[0], -x[1]))
        print(intervals)
        
        result = 0
        right = 0
        for i in intervals:
            result += i[1] > right
            right = max(right, i[1])
            
        return result