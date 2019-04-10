"""
https://leetcode-cn.com/problems/range-sum-query-mutable/
"""

class NumArray(object):
    # 树状数组 https://blog.csdn.net/bestsort/article/details/80796531
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.size = len(nums)
        self.data = [0] * self.size
        self.bt = [0] * (self.size + 1)
        for i in range(self.size):
            self.update(i, nums[i])
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        delta = val - self.data[i]
        k = i + 1
        while k <= self.size:
            self.bt[k] += delta
            k += (k&-k)
            # i&(-i)运算的功能为返回 i 的二进制数表示为１的最低位的权值
        self.data[i] = val
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.r(j+1) - self.r(i)
        
    def r(self, k):
        ret = 0
        while k > 0:
            ret += self.bt[k]
            k -= (k&-k)
        return ret
