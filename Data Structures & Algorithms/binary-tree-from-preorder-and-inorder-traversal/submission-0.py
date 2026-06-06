# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def dfs(inorder):
            if len(inorder) == 0:
                return None
            root_val = preorder.pop(0)
            root_idx = inorder.index(root_val)
            root_node = TreeNode(root_val)
            root_node.left = dfs(inorder[:root_idx])
            root_node.right = dfs(inorder[root_idx+1:])
            return root_node

        root = dfs(inorder)
        return root
