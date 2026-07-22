# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root: Optional[TreeNode]) -> int:

        left, right = 0, 0
        if root.left:
            left = 1 + self.dfs(root.left)
        if root.right:
            right = 1 + self.dfs(root.right)

        self.max = max(self.max, right + left)
        return max(left, right)
 


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.max = 0 
        self.dfs(root)
        
        return self.max