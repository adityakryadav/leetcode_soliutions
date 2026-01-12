class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = ""
        while(n):
            s = str(n%2) + s
            n = n//2

        return s.count('1')