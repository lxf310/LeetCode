"""
https://leetcode-cn.com/problems/car-fleet/
"""

class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        if not position:
            return 0
        
        dic = {}
        for i in range(len(position)):
            dic[position[i]] = (target - position[i]) * 1.0 / speed[i]
        position.sort(reverse=True)
        
        ret = 1
        time = dic[position[0]]
        for p in position:
            if dic[p] > time:
                time = dic[p]
                ret += 1
        return ret
