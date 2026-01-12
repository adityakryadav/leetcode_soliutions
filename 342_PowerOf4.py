class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        k = 0
        while(4**k <= n):
            if 4**k == n:
                return True
            k += 1
        return False