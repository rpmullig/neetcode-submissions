# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def dfs(self, root: Optional[TreeNode], depth: int) -> int:
        if not root:
            return depth
        
        depth += 1
        return max(self.dfs(root.right, depth), self.dfs(root.left, depth))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)