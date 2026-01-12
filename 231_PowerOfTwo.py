class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        k = 0
        while (2**k <= n):
            if 2**k == n:
                return True
            k+=1
        return False