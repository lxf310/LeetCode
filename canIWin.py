"""
https://leetcode-cn.com/problems/can-i-win/
"""

class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if maxChoosableInteger > desiredTotal:
            return True
        if maxChoosableInteger * (maxChoosableInteger + 1) / 2 < desiredTotal:
            return False
        return self.win(maxChoosableInteger, desiredTotal, 0, {})
        
    def win(self, length, target, used, dp):
        if dp.has_key(used):
            return dp[used]
        for i in range(1, length+1):
            # 计算每个bit位是否为使用过了
            if used & (1 << i) == 0:
                # 在此步取得胜利，或下一手会取得失败
                if target <= i or (not self.win(length, target-i, used|(1<<i), dp)):
                    dp[used] = True
                    return True
        dp[used] = False
        return False
        
