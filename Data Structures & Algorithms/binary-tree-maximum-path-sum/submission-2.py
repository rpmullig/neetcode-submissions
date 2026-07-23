# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.global_max = -math.inf

        def dfs(root):
            if not root:
                return 0
            
            if not root.left and not root.right:
                self.global_max = max(self.global_max, root.val)
                return root.val

            right_sum = dfs(root.right)
            left_sum = dfs(root.left)

            curr_max_sum = max(left_sum, right_sum, left_sum + root.val, right_sum + root.val)
            self.global_max = max(curr_max_sum, self.global_max, left_sum + root.val + right_sum)
            return curr_max_sum
        
        dfs(root)
        return self.global_max
