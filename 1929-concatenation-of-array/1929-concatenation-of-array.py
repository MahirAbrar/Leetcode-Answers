class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(nums) * 2
        length = len(nums)
        for i,num in enumerate(nums):
            ans[i] = num
            ans[i+length] = num

        return ans