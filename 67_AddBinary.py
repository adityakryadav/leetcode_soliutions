class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # k = 0
        # num = 0
        # for i in a[::-1]:
        #     num = num + (int(i))*(2**k)
        #     k+=1
        
        # k = 0
        # for i in b[::-1]:
        #     num = num + (int(i))*(2**k)
        #     k+=1

        xlen = len(a)
        ylen = len(b)
        k = max(xlen, ylen)
        if xlen < k:
            while len(a) < k:
                a = '0' + a
        elif ylen < k:
            while len(b) < k:
                b = '0' + b

        carry = 0
        rlt = ""
        for i in range(-1, k*(-1)-1, -1):
            sum = int(a[i]) + int(b[i]) + carry
            if sum == 2:
                rlt = '0' + rlt
                carry = 1
            elif sum == 3:
                rlt = '1' + rlt
                carry = 1
            else:
                rlt = str(sum) + rlt
                carry = 0
        
        if carry:
            rlt = '1' + rlt
        return rlt
        


