"""
https://leetcode-cn.com/problems/linked-list-cycle/
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle_hash(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        dic = {}
        while head:
            if dic.has_key(head):
                return True
            else:
                dic[head] = 1
            head = head.next
        return False
    
    def hasCycle(self, head):
        if head is None or head.next is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
