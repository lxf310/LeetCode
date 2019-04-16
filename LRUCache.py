"""
https://leetcode-cn.com/problems/lru-cache/
"""

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dic = {}
        self.head = None
        self.tail = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        val = -1
        if self.dic.has_key(key):
            element = self.dic[key]
            if element.next is not None:
                if element.pre is None:
                    self.head = element.next
                    element.next.pre = None
                else:
                    element.pre.next = element.next
                    element.next.pre = element.pre
                element.next = None
                element.pre = self.tail
                self.tail.next = element
                self.tail = element
            return element.val
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity == 0:
            return
        
        if self.dic.has_key(key):
            self.dic[key].val = value
            self.get(key)
            return
            
        if len(self.dic) == self.capacity:
            del self.dic[self.head.key]
            self.head = self.head.next
            if self.head is not None:
                self.head.pre = None
            
        element = Element(value, key)
        if self.head is None:
            self.head = element
            self.tail = element
        else:
            self.tail.next = element
            element.pre = self.tail
            self.tail = element
        self.dic[key] = element
        
class Element(object):
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.pre = None
        self.next = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
