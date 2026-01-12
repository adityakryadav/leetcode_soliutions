class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        di = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        l = len(s)
        for i in range(l):
            if (i==(l-1)):
                sum+=di[s[i]]
            elif di[s[i]]>=di[s[i+1]]:
                sum+=di[s[i]]
            else:
                sum-=di[s[i]]
        return sum
            