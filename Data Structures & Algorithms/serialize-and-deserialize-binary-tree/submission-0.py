# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        
        output = list()
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            if node:
                stack.append(node.left)
                stack.append(node.right)
                serialized  = str(hash(node)) + "|" + str(node.val) + "|" + str(hash(node.left)) + "|" + str(hash(node.right))
                output.append(serialized)

        print(','.join(output))

        return ','.join(output)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(',')
        mem_to_node = dict()
        mem_to_left_node = dict()
        mem_to_right_node = dict() 
        root = None
        for node in nodes:
            keys = node.split("|")
            if len(keys) == 1:
                continue
            new_node = TreeNode(val=int(keys[1]))
            if not root:
                root = new_node
            mem_to_node[keys[0]] = new_node
            mem_to_left_node[keys[0]] = keys[2]
            mem_to_right_node[keys[0]] = keys[3]
        
        for key, value in mem_to_node.items():
            left_mem, right_mem = mem_to_left_node[key], mem_to_right_node[key]
            value.left = mem_to_node.get(left_mem, None)
            value.right = mem_to_node.get(right_mem, None)

        return root