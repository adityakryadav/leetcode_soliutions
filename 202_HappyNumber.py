class Solution(object):
    def isHappy(self, n):
        """
        :type n: in t
        :rtype: bool
        """
        def sqsum(num, record=[]):
            sum = 0
            while(num):
                sum += (num%10)**2
                num = num//10
            if sum == 1:
                return True
            elif sum in record:
                return False
            else:
                record.append(sum)
                return sqsum(sum, record)

        return sqsum(n)