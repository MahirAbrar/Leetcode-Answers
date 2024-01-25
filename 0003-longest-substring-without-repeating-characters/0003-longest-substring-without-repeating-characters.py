class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = set()
        left = 0
        longest = 0
        cur = 0
        right = 0
        while right < len(s):
            while s[right] in map:
                map.remove(s[left])
                left += 1
                cur -= 1
            map.add(s[right])
            cur += 1
            longest = max(longest, cur)
            right += 1
        return longest