class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for num in numSet:
            if not (num - 1) in numSet:
                conLength = 1
                while num + conLength in numSet:
                    conLength += 1
                res = max(res, conLength)
        return res
