class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sizeTracker = {}
        arrLen = len(nums)
        toFind = arrLen / 3
        answer = []
        for num in nums:
            sizeTracker[num] = sizeTracker.get(num, 0) + 1

        # item is key
        for item in sizeTracker:
            if sizeTracker[item] > toFind:
                answer.append(item)
        return answer