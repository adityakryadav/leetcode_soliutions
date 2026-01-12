class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            del nums1[-1]
        # while(nums2 != [] and nums2[-1] == 0):
        #     del nums2[-1]

        for i in nums2:
            nums1.append(i)

        nums1.sort()

        # for i in range(n):
        #     for j in range(m):
        #         if nums2[i]>= nums1[j]:
        #             nums1.insert(j-1, nums2[i])