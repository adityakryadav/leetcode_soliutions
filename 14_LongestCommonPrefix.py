class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        st=""
        l1 = len(strs)
        l2 = len(strs[0])  #should be shortest word length
        br = 0
        for k in range(1,l1):
            if len(strs[k]) < l2:
                l2 = len(strs[k])
        
        for i in range(l2):
            tempst = strs[0][i]
            if br == 0:
                for j in range(l1):
                    if strs[j][i] != tempst:
                        br = -1
                        break
                else:
                    st += strs[0][i]

        return st