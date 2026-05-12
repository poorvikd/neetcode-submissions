# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return -1
            l_width = dfs(root.left)
            r_width = dfs(root.right)
            max_width = max(l_width,r_width)+1
            return max_width
        return dfs(root)+1
            