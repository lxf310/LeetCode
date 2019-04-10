"""
https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.curMAX = -2 ** 32
        self.cal(root)
        return self.curMAX
        
        
    def cal(self, root):
        if root is None:
            return 0
        leftSum = max(0, self.cal(root.left))
        rightSum = max(0, self.cal(root.right)) 
        # 以当前节点为跟的子树为最大路径
        self.curMAX = max(self.curMAX, root.val+leftSum+rightSum)
        # 以当前节点为子树时，只能选择值最大的那个叉
        return max(leftSum, rightSum) + root.val
    
# ###################
#       1
#     // \\
#      2  3 
#     / \\
#    4   5
#
#  最大路径为5-2-1-3
# ###################
