class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        k = len(s) == len(t)
        for i in t:
            if i in s:
                s = s.replace(i, "", 1)
            else:
                return False
        return k