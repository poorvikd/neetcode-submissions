# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_dia = 0
        def dfs(root, max_dia):
            if root == None:
                return -1, max_dia
            l_width,max_dia = dfs(root.left,max_dia)
            r_width,max_dia = dfs(root.right,max_dia)
            max_width = max(l_width+1,r_width+1)
            max_dia = max(max_dia, l_width + r_width + 2)
            return max_width, max_dia
        return dfs(root,max_dia)[1]
