# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [(root, math.inf, -math.inf)]
        while len(stack) > 0:
            node, max_val, min_val = stack.pop()

            if max_val < node.val or min_val > node.val:
                return False

            if node.left:
                stack.append((node.left, min(max_val, node.val), min_val))
            
            if node.right:
                stack.append((node.left, max_val, min(min_val, node.val)))

        return True 