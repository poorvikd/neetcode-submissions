# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res= [0]
        def dfs(root,k):
            if k == 0:
                return k
            if root.left:
                k = dfs(root.left,k)
            k -= 1
            if k == 0:
                res[0] = root.val
                return k
            if root.right:
                k = dfs(root.right,k)
            return k
        dfs(root,k)   
        return res[0]