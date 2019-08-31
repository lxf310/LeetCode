"""
https://leetcode-cn.com/problems/add-and-search-word-data-structure-design/
"""

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.key = '#'

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node[self.key] = {}
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def dfs(word, node):
            if word:
                if word[0] != '.':
                    if word[0] in node:
                        # check if substring exists
                        return dfs(word[1:], node[word[0]])
                    else:
                        return False
                else:
                    for v in node.values():
                        # Once an interested string is found, return True
                        if dfs(word[1:], v):
                            return True
                return False
            else:
                return self.key in node
            
        return dfs(word, self.root)
            
        
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
