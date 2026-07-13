# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            print("None")
        elif root1 and root2: 
            result: Optional[TreeNode] = TreeNode(val=(root1.val + root2.val))
            result.left = self.mergeTrees(root1.left, root2.left)
            result.right = self.mergeTrees(root1.right, root2.right)
            return result
        elif root1 and not root2: 
            result: Optional[TreeNode] = TreeNode(val=root1.val)
            result.left = root1.left
            result.right = root1.right
            return result
        else:
            result: Optional[TreeNode] = TreeNode(val=root2.val)
            result.left = root2.left
            result.right = root2.right
            return result