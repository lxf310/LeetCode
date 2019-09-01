"""
https://leetcode-cn.com/problems/maximal-square/
"""

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        n = len(matrix) + 1 #rows
        if n < 2:
            return 0
        m = len(matrix[0]) + 1 #colums
        maxLen = 0

        # dp[i][j] means the item at the bottom right coner of the square is matrix[i-1][j-1]
        dp = [[0]*m for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    maxLen = max(maxLen, dp[i][j])
        return maxLen*maxLen
