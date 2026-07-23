# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        result = list()
        q.append(root)
        while len(q) > 0:
            next_row = collections.deque()
            while len(q) > 0:
                node = q.popleft()
                if node:
                    if len(q) == 0:
                        result.append(node.val)
                    if node.left:
                        next_row.append(node.left)
                    if node.right:
                        next_row.append(node.right)

            q = next_row

        return result