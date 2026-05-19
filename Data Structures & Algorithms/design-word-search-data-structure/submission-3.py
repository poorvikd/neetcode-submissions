class Node:
    def __init__(self, key):
        self.key = key
        self.children = [None]*26
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node("")

    def addWord(self, word: str) -> None:
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

    def dfs(self, node, word, idx):
        print(f"Entered dfs {node.key} {word}")
        n = len(word)
        while idx<n:
            if word[idx] != '.':
                pos = ord(word[idx]) - ord('a')
                if node.children[pos] == None:
                    return False
                node = node.children[pos]
                idx += 1
            else:
                children = [ch for ch in node.children if ch!=None]
                for ch in children:
                    res = self.dfs(ch,word,idx+1)
                    if res == True:
                        return True
                return False
        return node.end

    def search(self, word: str) -> bool:
        return self.dfs(self.root,word,0)
    