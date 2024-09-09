class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for middle in range(len(s)):
            res += self.isPali(s, middle, middle)
            res += self.isPali(s, middle, middle + 1)
        return res

    def isPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res
