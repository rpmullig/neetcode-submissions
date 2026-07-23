# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
            if len(preorder) == 0:
                return None

            inorder_map = dict()
            for i, elm in enumerate(inorder):
                inorder_map[elm] = i 
            

            def treeBuilder(pre_left, pre_right, in_left, in_right):
                if pre_left > pre_right:
                    return None
                
                root_val = preorder[pre_left]
                root = TreeNode(val=root_val)
                mid = inorder_map[root_val]

                left_size = mid - in_left

                root.left = treeBuilder(pre_left + 1, pre_left + left_size, in_left, mid - 1)
                root.right = treeBuilder(pre_left + left_size + 1, pre_right, mid + 1, in_right)

                return root



            return treeBuilder(0, len(inorder) - 1, 0, len(inorder) - 1)