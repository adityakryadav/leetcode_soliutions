class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s.strip()
        l = s.split()
        return len(l[-1])

        for j in range(len(height)):
            area = abs(j-mi)*min(m,height[j])
            if area > marea:
                marea = area
                mi2 = j