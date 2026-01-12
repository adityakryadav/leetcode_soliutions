class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        if s[0] in ")}]" or l%2 != 0 or s.count('(') != s.count(')') or s.count('{') != s.count('}') or s.count('[') != s.count(']'):
                return False
        else:

            for i in range(l):
                if s[i] == '(':
                    for j in range(i+1,l,2):
                        if s[j] == ')':
                            if j-i == 3:
                                if (s[i+1]+s[i+2]) in ("()[]{"+"}"):
                                    break
                            else:
                                break
                            
                    else:
                        return False
                elif s[i] == '{':
                    for j in range(i+1,l,2):
                        if s[j] == '}':
                            if j-i == 3:
                                if (s[i+1]+s[i+2]) in ("()[]{"+"}"):
                                    break
                            else:
                                break
                    else:
                        return False
                elif s[i] == '[':
                    for j in range(i+1,l,2):
                        if s[j] == ']':
                            if j-i == 3:
                                if (s[i+1]+s[i+2]) in ("()[]{"+"}"):
                                    break
                            else:
                                break
                    else:
                        return False
        return True



        