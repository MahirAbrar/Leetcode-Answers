class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r  = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            print(mid)
            if nums[mid] == target:
                return mid
            #in left side
            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            #Right side
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1