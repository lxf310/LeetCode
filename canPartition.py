"""
https://leetcode-cn.com/problems/partition-equal-subset-sum/
"""

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2 != 0:
            return False
        nums.sort(reverse=True)
        
        def dfs(nums, target, cur, pos):
            for i in range(pos+1, len(nums)):
                if cur+nums[i] == target:
                    return True
                if cur+nums[i] > target:
                    continue
                if dfs(nums, target, cur+nums[i], i):
                    return True
            return False
  

        total /= 2
        if nums[0] > total:
            return False
        
        if total in nums:
            return True
        
        for i in range(len(nums)):
            if dfs(nums, total, nums[i], i):
                return True
        
        return False
