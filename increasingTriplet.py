"""
https://leetcode-cn.com/problems/increasing-triplet-subsequence/
"""

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        small = big = sys.maxint
        for n in nums:
            if n < small:
                small = n
            elif n > small and n <= big:
                big = n
            elif n > big:
                return True
        return False
