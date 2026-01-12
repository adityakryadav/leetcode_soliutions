class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_chars, t_chars = [], []
        if len(s) != len(t) :
            return False
        else :
            for i in range(len(s)) :
                if (s[i] in s_chars) == (t[i] not in t_chars):
                    return False
                elif (s[i] not in s_chars and t[i] not in t_chars) : 
                    s_chars.append(s[i])
                    t_chars.append(t[i])
                elif (s_chars.index(s[i]) != t_chars.index(t[i])):
                    return False
        return True
