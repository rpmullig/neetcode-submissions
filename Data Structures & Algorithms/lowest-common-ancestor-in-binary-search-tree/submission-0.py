# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.common_ancestor: TreeNode = None
        
        def dfs(root, p, q):
            if not root:
                return False
            
            mid = root.val == q.val or root.val == p.val

            right = dfs(root.right, p, q)
            left = dfs(root.left, p, q)

            if (left and right) or (mid and right) or (mid and left):
                if not self.common_ancestor:
                    self.common_ancestor = root

            return mid or left or right

        dfs(root, p, q)
        return self.common_ancestor