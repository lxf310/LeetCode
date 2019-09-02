"""
https://leetcode-cn.com/problems/find-the-duplicate-number/
"""

"""
There must be a circle existing. Let the length of the circle equal 'c'.
Let the distance between start point to the circle entry euqal 'm'.
Let the distance between circle entry to the next meet point between fast pointer and slow pointer equal 'x'.
=> 2(m+x) = m+c+x
=> m = c-x

Now, let the third pointer start to go from the start point and let slow pointer keep moving.
Then the meet point between the third point and slow point is the circle entry point that is the duplication element.
"""
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
                
        target = 0
        while True:
            target = nums[target]
            slow = nums[slow]
            if target == slow:
                return target
