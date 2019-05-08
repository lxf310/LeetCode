"""
https://leetcode-cn.com/problems/minimum-path-sum/
动态规划
"""

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid) # row number
        n = len(grid[0]) # column number
        dp = [[0 for x in range(n)] for y in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
            
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] += (min(dp[i-1][j], dp[i][j-1]) + grid[i][j])
        
        return dp[m-1][n-1]
