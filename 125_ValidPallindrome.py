class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s2 = ''
        for i in s:
            if (i.isalnum()):
               s2+=i
        
        s2 = s2.lower()
        return s2[::-1] == s2