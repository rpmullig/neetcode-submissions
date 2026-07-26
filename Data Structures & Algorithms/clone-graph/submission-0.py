"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node: 
            return None

        stack = [node]
        copy_map = dict()
        original_map = dict() 
        while len(stack) > 0:
            curr = stack.pop()
            if curr.val not in original_map:
                copy_map[curr.val] = Node(val=curr.val)
                original_map[curr.val] = curr
                for neighbor in curr.neighbors:
                    if neighbor and neighbor.val not in original_map:
                        stack.append(neighbor)
        

        for val, copy_node in copy_map.items():
            if original_map[val].neighbors == None:
                continue 
            
            neighbor_list = list()
            for neighbor in original_map[val].neighbors:
                neighbor_list.append(copy_map[neighbor.val])
            
            copy_node.neighbors = neighbor_list


        return copy_map[node.val]