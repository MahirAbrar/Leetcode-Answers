class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i, inter in enumerate(intervals):
            if newInterval[1] < inter[0]:
                res += [newInterval] + intervals[i:]
                return res
            elif newInterval[0] > inter[1]:
                res.append(inter)
            else:
                newInterval = [min(newInterval[0], inter[0]), max(newInterval[1], inter[1])]
            
        res.append(newInterval)
        return res
