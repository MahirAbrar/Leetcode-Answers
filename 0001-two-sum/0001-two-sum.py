class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i in range(len(nums)):
            digit = nums[i]
            if target - digit in store:
                return [store[target-nums[i]] ,i]
            store[digit] = i