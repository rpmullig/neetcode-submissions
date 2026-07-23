# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, -math.inf)]
        result = 0 
        while len(stack) > 0:
            node, current_max = stack.pop()
            if node.val >= current_max:
                result += 1
                current_max = node.val
            
            if node.left:
                stack.append((node.left, current_max))
            
            if node.right:
                stack.append((node.right, current_max))


        return result 