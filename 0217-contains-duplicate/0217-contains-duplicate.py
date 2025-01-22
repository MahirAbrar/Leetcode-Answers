class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create an empty set to store unique elements from the input list
        unique_elements = set()

        # Iterate over the input list
        for num in nums:
            # If the current element exists in the set, we found a duplicate: return True
            if num in unique_elements:
                return True
            # Otherwise, add the num to the set
            else:
                unique_elements.add(num)

        # If the loop completes and we did not return early, there are no duplicate elements
        return False