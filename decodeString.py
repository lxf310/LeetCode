"""
https://leetcode-cn.com/problems/decode-string/
"""

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = ''
        num = ''
        st = []
        for c in s:
            if c.isdigit():
                num += c
            elif c.isalpha():
                ret += c
            elif c == '[':
                st.append([int(num), ret])
                # reset
                num, ret = '', ''
            else:
                n, pre = st.pop()
                ret = pre + ret * n
        return ret
