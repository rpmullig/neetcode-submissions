class Deque:
    
    class Node:
        def __init__(self, val= None):
            self.val = val
            self.next = None
            self.prev = None


    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = self.head

    def isEmpty(self) -> bool:
        return self.length == 0 

    def append(self, value: int) -> None:
        if self.isEmpty():
            self.head = self.Node(val=value)
            self.tail = self.head
        else:
            new_node = self.Node(val=value)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def appendleft(self, value: int) -> None:
        if self.isEmpty():
            self.head = self.Node(val=value)
            self.tail = self.head
        else:
            new_node = self.Node(val=value)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop(self) -> int:
        result: int = None
        if self.length == 0:
            return -1
        
        if self.length == 1:
            result = self.tail.val
            self.tail = None
            self.head = None
        else:
            result = self.tail.val
            self.tail = self.tail.prev
            self.tail.next = None
        
        self.length -= 1
        return result

    def popleft(self) -> int:
        result: int = None
        if self.isEmpty():
            return -1
        
        if self.length == 1:
            result = self.head.val
            self.tail = None
            self.head = None
        else:
            result = self.head.val
            self.head = self.head.next
            self.head.prev = None
        
        self.length -= 1
        return result
        
