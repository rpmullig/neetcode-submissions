"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummyHead = Node(0)
        curr = dummyHead
        target = head    

        # first pass to create it, we need to have existance
        i = 0
        target_node_order = dict()
        number_to_node = dict() 
        while target:
            target_node_order[id(target)] = i
            curr.next = Node(x=target.val)
            number_to_node[i] = curr.next
            i += 1
            target = target.next 
            curr = curr.next

        target = head
        node_to_random_connections = dict()
        while target:
            start = target_node_order[id(target)]
            end = target_node_order[id(target.random)] if target.random else None
            node_to_random_connections[start] = end 
            target = target.next 

        target = head 
        curr = dummyHead.next
        i = 0 
        while target:
            random_index = node_to_random_connections[i]
            
            if random_index is not None:
                curr.random = number_to_node[random_index]
            else:
                curr.random = None
            i += 1
            curr = curr.next
            target = target.next 


        return dummyHead.next 