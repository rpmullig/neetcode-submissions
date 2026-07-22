# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def dfs(self, root) -> int:
        if not root: 
            return 0

        right, left = 0, 0 
        if root.right:
            right = 1 + self.dfs(root.right)
        
        if root.left: 
            left = 1 + self.dfs(root.left)
        
        if abs(right - left) > 1:
            self.status = False
        
        return max(right, left)


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.status = True 
        self.dfs(root)
        return self.status