"""
https://leetcode-cn.com/problems/binary-trees-with-factors/
"""

class Solution(object):
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        dp = [1 for x in range(len(A))]
        dic = {}
        MOD = 10 ** 9 + 7
        ret = 0
        for i in range(len(A)):
            dic[A[i]] = i
            # node j is the child of node i, since A is sorted
            for j in range(0, i):
                if A[i] % A[j] == 0:
                    tmp = A[i] / A[j]
                    if dic.has_key(tmp):
                        dp[i] = (dp[i] + (dp[dic[tmp]] * dp[j]) % MOD) % MOD
            ret = (ret + dp[i]) % MOD
        return ret
