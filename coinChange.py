"""
https://leetcode-cn.com/problems/coin-change/
"""

class Solution(object):
    def coinChangeDFS(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        
        coins.sort(reverse=True)        
        if amount < coins[-1]:
            return -1
        
        self.res = sys.maxint
        n = len(coins)
        
        def dfs(pos, remain, count):
            if remain == 0:
                self.res = min(self.res, count)
            for i in range(pos, n):
                if coins[i] <= remain and count < self.res and remain <= coins[i]*(self.res-count):
                    dfs(i, remain-coins[i], count+1)
                    
        for i in range(n):
            dfs(i, amount, 0)
        
        return self.res if self.res != sys.maxint else -1
    
    
    def coinChange(self, coins, amount):
        dp = [sys.maxint for x in range(amount+1)]
        dp[0] = 0
        
        for i in range(1, amount+1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i-coin]+1, dp[i])
        return dp[amount] if dp[amount] != sys.maxint else -1
        
