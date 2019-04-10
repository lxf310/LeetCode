####################################
# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
###################################

import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.find(nums, k, 0, len(nums)-1)
        
    def find(self, nums, k, l, r):
        pos = self.partition(nums, l, r)
        if pos == (k-1):
            return nums[pos]
        elif pos > (k-1):
            return self.find(nums, k, l, pos-1)
        else:
            return self.find(nums, k, pos+1, r)
    
    def partition(self, nums, l, r):
        i = random.randint(l,r)
        nums[i], nums[l] = nums[l], nums[i]
        pivot = nums[l]
        j = l
        i = l + 1
        while i <= r:
            if nums[i] >= pivot:
                j += 1
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
        nums[l], nums[j] = nums[j], nums[l]
        return j
