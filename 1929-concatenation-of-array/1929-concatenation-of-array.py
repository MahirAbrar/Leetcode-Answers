class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = [None] * len(nums) * 2
        for i, n in enumerate(nums):
            res[i] = n
            res[i + len(nums)] = n
        return res
        