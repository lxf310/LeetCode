#######################
# https://leetcode-cn.com/problems/capacity-to-ship-packages-within-d-days/
#######################

class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        maxW = sum(weights)
        minW = max(weights)
        #print maxW, minW
        while minW < maxW:
            mid = (maxW + minW) // 2
            tmp = 0
            days = 1
            for w in weights:
                tmp += w
                if tmp > mid:
                    days += 1
                    tmp = w
            if days > D:
                minW = mid + 1
            else:
                maxW = mid
        return minW
