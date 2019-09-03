"""
https://leetcode-cn.com/problems/house-robber-iii/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def doRob(root):
            res = [0, 0]
            if root is None:
                return res
            robLeft = doRob(root.left)
            robRight = doRob(root.right)
            
            # 0 means not to rob the current node
            # 1 means to rob the current node
            res[0] = max(robLeft) + max(robRight)
            res[1] = root.val + robLeft[0] + robRight[0]
            return res
                
        return max(doRob(root))
