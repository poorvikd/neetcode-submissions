# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p,q = min(p.val,q.val),max(p.val,q.val)
        def dfs(root,p,q):
            if root.val >= p and root.val < q:
                return root
            if root.val > p and root.val <= q:
                return root
            if root.val < p:
                return dfs(root.right,p,q)
            if root.val > q:
                return dfs(root.left,p,q)
        
        return dfs(root,p,q)

            
                