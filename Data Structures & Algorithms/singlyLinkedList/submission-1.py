class LinkedList:
    
    class Node:
        def __init__(self,  data: int, next_node: 'Node' = None):
            self.data: int = data
            self.next_node: 'Node' = next_node
        
        def get_next(self) -> 'Node':
            return self.next_node
        
        def get_data(self) -> int:
            return self.data
        
        def set_data(self, data: int) -> None:
            self.data = data
        
        def set_next(self, next_node: 'Node') -> None:
            self.next_node = next_node

    def __init__(self):
        self.head: LinkedList.Node = None
    
    def get(self, index: int) -> int:
        curr: LinkedList.Node = self.head
        while curr and index > 0:
            curr = curr.get_next()
            index -= 1
        
        if curr:
            return curr.get_data()
        return -1

    def insertHead(self, val: int) -> None:
        if not self.head:
            self.head =  LinkedList.Node(val, None)
            return None
        new_node: LinkedList.Node = LinkedList.Node(val, self.head)
        self.head = new_node
        

    def insertTail(self, val: int) -> None:
        curr: LinkedList.Node = self.head
        while curr and curr.get_next():
            curr = curr.get_next()
        next_node: Node = LinkedList.Node(val, None)
        curr.set_next(next_node)

    def remove(self, index: int) -> bool:
        if index == 0:
            self.head = self.head.get_next()
            return True

        curr: LinkedList.Node = self.head
        while curr and index > 1:
            curr = curr.get_next()
            index -= 1
        if curr and curr.get_next():
            curr.set_next(curr.get_next().get_next())
            return True
        return False

    def getValues(self) -> List[int]:
        result: List[int] = list()
        curr: LinkedList.Node = self.head
        while curr:
            result.append(curr.get_data())
            curr = curr.get_next()
        
        return result
        
        
