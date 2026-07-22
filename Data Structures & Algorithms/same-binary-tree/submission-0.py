# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        left = [p]
        right = [q]
        while len(left) > 0 and len(right) > 0:
            left_node = left.pop()
            right_node = right.pop()

            if left_node.val != right_node.val:
                return False
            
            # bool mask to make sure both have nodes to remove some if statements 
            mask = (left_node.left is not None and right_node.left is not None) or (left_node.left is None and right_node.left is None)
            mask = mask and (((left_node.right is not None and right_node.right is not None) or (left_node.right is None and right_node.right is None)))

            if not mask:
                return False
            

            if left_node.left:
                left.append(left_node.left)
                right.append(right_node.left)
            
            if left_node.right:
                left.append(left_node.right)
                right.append(right_node.right)


        return len(left) == 0 and len(right) == 0