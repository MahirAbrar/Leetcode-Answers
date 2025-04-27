class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        anagrams = defaultdict(list)

        for s in strs:
            base = [0] * 26
            for c in s:
                code = ord(c) - ord("a")
                base[code] = base[code] + 1
            anagrams[tuple(base)].append(s)

        return list(anagrams.values())    