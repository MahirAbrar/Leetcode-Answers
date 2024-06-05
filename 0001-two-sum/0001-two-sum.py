class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for index, val in enumerate(nums):
            requiredNumber = target - val
            if requiredNumber in prevMap:
                return [prevMap[requiredNumber],index]
            prevMap[val] = index
        