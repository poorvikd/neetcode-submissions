"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        db = {}
        if node == None:
            return None
        new_node = Node(node.val)
        db[node.val] = new_node
        visited = set()
        def dfs(node):
            visited.add(node.val)
            for n in node.neighbors:
                if db.get(n.val, None) == None:
                    new_node = Node(n.val)
                    db[n.val] = new_node
                db[node.val].neighbors.append(db[n.val])  
                if n.val not in visited:
                    dfs(n)
            return
        dfs(node)
        return new_node
        