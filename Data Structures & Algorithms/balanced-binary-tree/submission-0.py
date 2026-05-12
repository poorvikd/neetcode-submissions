# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if root == None:
                return -1,True
            l_height, isbalanced = dfs(root.left)
            if not isbalanced:
                return -1, isbalanced
            r_height, isbalanced = dfs(root.right)
            if not isbalanced:
                return -1, isbalanced
            if abs(l_height - r_height) > 1:
                return -1, False
            max_height = max(l_height, r_height)+1
            return max_height, True
        
        return dfs(root)[1]
