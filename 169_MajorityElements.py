class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i, cnt = 0, 0
        while(i<len(nums)):
            cnt2 = nums.count(nums[i])
            if (cnt2>cnt):
                cnt = cnt2
                k = nums[i]
            i += cnt2
        return k
