"""
https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # in different branches
        if left is not None and right is not None:
            return root
        
        # all in left
        if left is not None:
            return left
        
        # all in right
        if right is not None:
            return right
        
        # cannot find the nodes
        return None
