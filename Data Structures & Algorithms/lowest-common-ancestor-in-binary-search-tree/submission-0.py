# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p,q = min(p.val,q.val),max(p.val,q.val)

        def dfs(root, p, q):
            if p > root.val:
                return dfs(root.right,p,q)
            elif q < root.val:
                return dfs(root.left,p,q)
            else:
                return root
        
        return dfs(root, p, q)