class Solution:
    def tribonacci(self, n: int) -> int:
        temp = [0, 1, 1]
        if n < 3:
            return temp[n]
        for i in range(3, n+1):
            val = sum(temp)
            temp[0] = temp[1]
            temp[1] = temp[2]
            temp[2] = val
        return temp[2]