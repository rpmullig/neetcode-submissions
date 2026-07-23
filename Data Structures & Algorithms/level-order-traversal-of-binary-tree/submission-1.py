# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return list()

        result: List[List[int]] = list()
        q = collections.deque()
        q.append(root)
        while len(q) > 0:
            next_row = list()
            next_queue = collections.deque()
            while len(q) > 0:
                node = q.popleft()
                if node:
                    next_row.append(node.val)

                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)

            q = next_queue
            result.append(next_row)
        
        return result