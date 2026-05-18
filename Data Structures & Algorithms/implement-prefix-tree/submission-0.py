class Node:
    def __init__(self, key):
        self.key = key
        self.children = [None]*26
        self.end = False
class PrefixTree:
    def __init__(self):
        self.root = Node("")

    def insert(self, word: str) -> None:
        node = self.root
        idx = 0
        n = len(word)
        while idx<n:
            pos = ord(word[idx]) - ord('a')
            if node.children[pos] == None:
                node.children[pos] = Node(word[idx])
            node = node.children[pos]
            idx += 1
        node.end = True

    def search(self, word: str) -> bool:
        node = self.root
        idx = 0
        n = len(word)
        while idx<n:
            pos = ord(word[idx]) - ord('a')
            if node.children[pos] == None:
                return False
            node = node.children[pos]
            idx += 1
        
        return node.end


    def startsWith(self, prefix: str) -> bool:
        node = self.root
        idx = 0
        n = len(prefix)
        while idx<n:
            pos = ord(prefix[idx]) - ord('a')
            if node.children[pos] == None:
                return False
            node = node.children[pos]
            idx += 1
        
        return True
        
        