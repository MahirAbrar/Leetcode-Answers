class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map1 = {}
        map2 = {}

        for i, j in zip(s, t):
            map1[i] = map1.get(i, 0) + 1
            map2[j] = map2.get(j, 0) + 1
        
        for key in map1:
            if map1.get(key) != map2.get(key,0):
                return False
        return True