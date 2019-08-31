"""
https://leetcode-cn.com/problems/implement-trie-prefix-tree/
"""

# reference: https://www.jianshu.com/p/f4d371220ece
class TrieNode(object):
    def __init__(self):
        self.count = 0
        # key: character
        # value: TrieNode
        self.children = {}
        self.isWord = False


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node.children[c].count += 1
            node = node.children[c]
        node.isWord = True
                    
                       

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        # for exmaple: 'abc' in dict, but 'ab' not
        return node.isWord
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.count > 0

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
