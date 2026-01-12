class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        lt1 = []
        def fact(num):
            rlt = 1
            for i in range(2,num+1):
                rlt = rlt*i
            return rlt

        def ncr(n, r):
            rlt = fact(n)/(fact(r)*fact(n-r))
            return rlt

        for i in range(numRows):
            lt2 = []
            for j in range(i+1):
                lt2.append(ncr(i, j))
            lt1.append(lt2)

        return lt1