# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = collections.deque()
        q.append((root, 0))
        max_depth = 0
        while len(q) > 0:
            node, current_depth = q.popleft()
            if node:
                current_depth += 1
                max_depth = max(current_depth, max_depth)

                if node.left:
                    q.append((node.left, current_depth))
                if node.right:
                    q.append((node.right, current_depth))

        
        return max_depth