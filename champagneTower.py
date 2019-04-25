"""
https://leetcode-cn.com/problems/champagne-tower/
"""

class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        total = query_row + 1
        dp = [[0.0] * total for i in range(total)]
        dp[0][0] = poured * 1.0
        for i in range(query_row):
            # 自顶向下计算，将多余的香槟平均分给左右两边的杯子
            for j in range(i+1):
                if dp[i][j] > 1:
                    delta = (dp[i][j] - 1) / 2
                    dp[i+1][j] += delta
                    dp[i+1][j+1] += delta
                    dp[i][j] = 1
        return min(1.0, dp[query_row][query_glass])
