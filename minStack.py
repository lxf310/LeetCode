"""
https://leetcode-cn.com/problems/min-stack/
"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = []
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.min or self.min[-1] > x:
            self.min.append(x)
        else:
            self.min.append(self.min[-1]) 
        
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.min:
            return self.min[-1]
        return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
