class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        num, n = 0, 0
        for i in columnTitle[::-1]:
            num += (ord(i)-64)*(26**n)
            n += 1

        return num