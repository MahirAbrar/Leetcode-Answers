class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for ind, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stkInd, stkTemp = stack.pop()
                res[stkInd] = ind - stkInd
            stack.append((ind, temp))
        return res