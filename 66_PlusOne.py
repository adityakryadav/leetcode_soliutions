class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i in range(len(digits)):
            num = (10*num)+digits[i]
            
        num+=1
        rlt = ""
        while(num):
            rlt = str(num%10)+rlt
            num = num//10

        rl = []
        for i in range(len(rlt)):
            rl.append(int(rlt[i]))
        return rl