class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        


        if len(s) != len(t):
            return False
        
        str1 = {}
        str2 = {}

        for num in s:
            str1[num] = str1.get(num, 0) + 1
        
        for num in t:
            str2[num] = str2.get(num, 0) + 1
        
        return True if str1 == str2 else False