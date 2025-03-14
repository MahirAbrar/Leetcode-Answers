class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        for a in range(len(nums)):
            # This early break is incorrect - we can have positive numbers that sum to target
            # if nums[a] > 0:
            #     break
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            
            for b in range(a + 1, n):
                if b != a + 1 and nums[b] == nums[b - 1]:
                    continue
                
                left, right = b + 1, n - 1

                while left < right:
                    total = nums[a] + nums[b] + nums[left] + nums[right]
                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:  # total == target
                        res.append([nums[a], nums[b], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        # Skip duplicates
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
        return res