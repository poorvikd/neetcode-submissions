# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return 0,True
            l_height,res = dfs(root.left)
            if not res:
                return -1,False
            r_height,res = dfs(root.right)
            if not res:
                return -1,False
            if abs(l_height - r_height)>1:
                return -1,False
            curr_height = max(l_height,r_height)+1
            return curr_height,True
        return dfs(root)[1]

