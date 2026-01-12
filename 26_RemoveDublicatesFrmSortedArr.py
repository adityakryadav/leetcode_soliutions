class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        # k = 0
        i = 1
        while (i<l):
            try: 
                condition = nums[i] <= nums[i-1] and i<l
            except:
                condition = False
            while (condition):  #if (nums[i] <= nums[i-1]):
                # for j in range(i,l):
                #     if (nums[i-1] < nums[j]):
                #         nums[i] = nums[j]
                #         k += 1
                #         break
                del nums[i]
                try: 
                    condition = nums[i] <= nums[i-1] and i<l
                except:
                    condition = False
            l = len(nums)
            i += 1

        return (l)