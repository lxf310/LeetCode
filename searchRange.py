"""
https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        return self.bisearch(nums, 0, len(nums) - 1, target)
        
    def bisearch(self, nums, left, right, target):
        if left < 0 or right > len(nums) - 1 or left > right:
            return [-1, -1]
        mid = left + (right - left) / 2
        i = mid
        j = mid
        while i > 0 and nums[i] == nums[i - 1]:
            i -= 1
        while j < len(nums) - 1 and nums[j] == nums[j + 1]:
            j += 1
        if target == nums[mid]:
            return [i, j]
        elif target > nums[mid]:
            return self.bisearch(nums, j + 1, right, target)
        else:
            return self.bisearch(nums, left, i - 1, target)
