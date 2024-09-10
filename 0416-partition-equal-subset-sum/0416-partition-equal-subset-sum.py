class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums)):
            newDp = set()
            for t in dp:
                newDp.add(t + nums[i])
            if target in newDp:
                return True
            dp = dp.union(newDp)
        
        return True if target in dp else False
            

