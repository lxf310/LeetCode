"""
https://leetcode-cn.com/problems/palindromic-substrings/
"""

class Solution:
    def countSubstrings1(self, s: str) -> int:
        def valid(start, end, s):
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        
        ret = 0
        for start in range(len(s)):
            for end in range(start, len(s)):
                if valid(start, end, s):
                    ret += 1
        return ret
        
    
    def countSubstrings(self, s: str) -> int:
        def _count(start, end, s):
            ret = 0
            while start >=0 and end < len(s) and s[start] == s[end]:
                ret += 1
                start -= 1
                end += 1
            return ret
        
        ret = 0
        for i in range(len(s)):
            ret += _count(i, i, s)
            ret += _count(i, i+1, s)
        return ret
