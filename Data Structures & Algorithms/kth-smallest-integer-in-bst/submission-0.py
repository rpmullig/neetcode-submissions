# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        result = list()
        def dfs(root, result):
            if not root:
                return
            
            dfs(root.left, result)
            result.append(root.val)
            dfs(root.right, result)


        dfs(root, result)
        return  result[k-1]