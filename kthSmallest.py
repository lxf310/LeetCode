"""
https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        p = root
        while p is not None:
            stack.append(p)
            p = p.left
        
        while stack:
            p = stack.pop()
            k -= 1
            if k == 0:
                return p.val
            p = p.right
            while p:
                stack.append(p)
                p = p.left
        return None
