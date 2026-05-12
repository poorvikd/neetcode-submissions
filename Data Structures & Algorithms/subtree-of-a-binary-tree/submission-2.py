# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def matchSubTree(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if root.val != subRoot.val:
                return False
            return matchSubTree(root.left,subRoot.left) & matchSubTree(root.right,subRoot.right)

            



        def matchRoot(root, subRoot):
            if not root and not subRoot:
                return True
            elif not root or not subRoot:
                return False
            elif root.val == subRoot.val:
                match = matchSubTree(root, subRoot)
                if match:
                    return True
            return matchRoot(root.left, subRoot) or matchRoot(root.right, subRoot)
        
        return matchRoot(root, subRoot)