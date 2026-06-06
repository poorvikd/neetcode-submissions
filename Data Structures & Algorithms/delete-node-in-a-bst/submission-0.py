# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find_leftmost(root):
            if root.left:
                return find_leftmost(root.left)
            return root

        def dfs(root,key):
            if not root:
                return None
            elif root.val < key:
                root.right = dfs(root.right,key)
            elif root.val > key:
                root.left = dfs(root.left,key)
            else:
                if root.left and not root.right:
                    return root.left
                elif root.right and not root.left:
                    return root.right
                elif not root.left and not root.right:
                    return None
                else:
                    next_root = find_leftmost(root.right)
                    root.val = next_root.val
                    root.right = dfs(root.right,next_root.val)
                    return root
            return root
        return dfs(root,key)
                