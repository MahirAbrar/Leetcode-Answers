class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(self, nums, path = []):
            if not nums:
                res.append(path)
                return
            for x in range(len(nums)):
                backtrack(self, nums[:x] + nums[x + 1:], path + [nums[x]])
        
        backtrack(self, nums, [])
        return res