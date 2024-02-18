class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        for i in range(0, len(nums) + 1):
            total += i
        return total - sum(nums)