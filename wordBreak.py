"""
https://leetcode-cn.com/problems/word-break/
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s) + 1
        dp = [False for i in range(n)]
        dp[0] = True
        wordDict.append('')
        wordDict.sort(key=len)
        minn = len(wordDict[0])
        for i in range(n):
            for j in range(minn, i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
