class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        memo = [-1] * (len(nums))
        flag = True

        def dfs(i):
            if i >= len(nums) or (flag and i == (len(nums) - 1)):
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(nums[i] + dfs(i+2), dfs(i+1))
            print(memo)
            return memo[i]
        
        withVal = dfs(0)
        memo = [-1] * (len(nums))
        flag = False
        withoutVal = dfs(1)
        return max(withVal, withoutVal)