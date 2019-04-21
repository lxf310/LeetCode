"""
https://leetcode-cn.com/problems/sort-list/
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        p = head
        pp = head
        pre = None
        while pp and pp.next:
            pre = p
            p = p.next
            pp = pp.next.next
        pre.next = None
        l = self.sortList(head)
        r = self.sortList(p)
        return self.merge(l, r)
    
    def merge(self, l, r):
        head = ListNode(0)
        cur = head
        while l and r:
            if l.val <= r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        if l:
            cur.next = l
        if r:
            cur.next = r
        return head.next
