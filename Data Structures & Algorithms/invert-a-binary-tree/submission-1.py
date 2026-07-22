# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        q = collections.deque()
        q.append(root)
        while len(q) > 0:
            node = q.popleft()

            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
            
            right, left = node.right, node.left
            node.right = left
            node.left = right

        return root