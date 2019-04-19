"""
https://leetcode-cn.com/problems/number-of-1-bits/
""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        while n:
            ret += 1
            n &= (n-1) #remove the last 1
        return ret



"""
https://leetcode-cn.com/problems/power-of-two/
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 整数的负数相当于改正数二进制位各位取反，之后再加一；
        # 所以n & -n相当于截取n的最低位1的位置
        return (n>0) and n&-n == n



"""
https://leetcode-cn.com/problems/single-number/
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = nums[0]
        for i in range(1, len(nums)):
            ret ^= nums[i]
        return ret
