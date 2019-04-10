"""
https://leetcode-cn.com/problems/longest-palindromic-substring/submissions/
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        middle = 0
        maxlength = 1
        if len(s) < 2:
            return s
        for i in range(len(s)):
            n1 = self.expand(s, i, i)
            n2 = self.expand(s, i, i + 1)
            n = n1 if n1 > n2 else n2
            if n > maxlength:
                maxlength = n
                middle = i
        half = maxlength / 2
        if maxlength % 2 == 0:
            return s[middle - half + 1: middle + half + 1]
        else:
            return s[middle - half: middle + half + 1]

    def expand(self, s, left, right):
        l = left
        r = right
        n = len(s)
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        return (r -l - 1)
