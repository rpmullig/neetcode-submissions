# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        result = list()
        def dfs(root, result, k):
            if not root:
                return
            
            if len(result) == k:
                return 

            dfs(root.left, result, k)
            result.append(root.val)
            dfs(root.right, result, k)


        dfs(root, result, k)
        return  result[k-1]