# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        lt = []
        while (head):
            if id(head) in lt:
                return True
            else:
                lt.append(id(head))
                head = head.next
        return False