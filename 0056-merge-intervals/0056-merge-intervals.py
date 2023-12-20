class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sorted(intervals, key= lambda x: x[0])   Never use sorted
        
        intervals.sort(key=lambda x: x[0])
        output = [intervals[0]]
        
        for start, end in intervals:
            lastEnd = output[-1][1]
            if start <= lastEnd:
                output[-1][1] = max(end, lastEnd)
                
            else:
                output.append([start, end])
                
        return output
