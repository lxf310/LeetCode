"""
https://leetcode-cn.com/problems/card-flipping-game/
"""

class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        same = []
        diff = []
        for i in range(len(fronts)):
            if fronts[i] != backs[i]:
                diff.append(fronts[i])
                diff.append(backs[i])
            else:
                # 正反面都相同的不会是所需要的牌
                same.append(fronts[i])
        # 去掉正反面不同的牌中与淘汰掉的牌的数组相同的那一面，因为该面与正面的牌一定有重复的
        for s in same:
            while s in diff:
                diff.remove(s)
        if diff:
            diff.sort()
            return diff[0]
        return 0
        
