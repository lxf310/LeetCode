"""
https://leetcode-cn.com/problems/top-k-frequent-elements/submissions/
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """        
        def getIndex(left, right):
            #print 'in: ', self.array
            pivot = self.array[left]
            i = left
            j = right
            while i < j:
                while i < j and self.array[j][1] < pivot[1]:
                    j -= 1
                if i < j:
                    #print '\t', i, j, self.array
                    self.array[i] = self.array[j]
                    #print '=>\t', i, j, self.array
                    i += 1
                while i < j and self.array[i][1] > pivot[1]:
                    i += 1
                if i < j:
                    #print '\t', i, j, self.array
                    self.array[j] = self.array[i]
                    #print '=>\t', i, j, self.array
                    j -= 1
            self.array[j] = pivot
            
            if i > k and left < i-1:
                getIndex(left, i-1)
            elif i < k and right > i+1:
                getIndex(i+1, right)
        
        
        numDict = {}
        for num in nums:
            numDict[num] = numDict.setdefault(num, 0) + 1
            
        self.array = numDict.items()
        #print self.array
        getIndex(0, len(self.array)-1)
        #print self.array
        
        ret = []
        for i in range(k):
            ret.append(self.array[i][0])
        return ret
