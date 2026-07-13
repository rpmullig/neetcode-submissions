class Deque:
    
    class Node:

        def __init__(self):
            self.data: int = None
            self.next: 'Node' = None
            self.prev: 'Node' = None


    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def append(self, value: int) -> None:
        if self.size == 0:
            self.head = Deque.Node()
            self.tail = self.head
            self.head.data = value
            self.size += 1
            return None

        self.tail.next = Deque.Node()
        self.tail.next.prev = self.tail
        self.tail = self.tail.next
        self.tail.data = value

    def appendleft(self, value: int) -> None:
        if self.size == 0:
            self.head = Deque.Node()
            self.tail = self.head
            self.head.data = value
            self.size += 1
            return None

        self.head.next = self.head
        new_node = Deque.Node()
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        self.head.data = value
        self.size += 1
        

    def pop(self) -> int:
        if self.size == 0 or not self.tail:
            return -1

        self.size -= 1
        pop_node = self.tail
        self.tail = self.tail.prev
        return pop_node.data

    def popleft(self) -> int:
        if self.size == 0 or not self.head:
            return -1 
        
        self.size -= 1
        pop_node_data = self.head.data
        self.head = self.head.next
        self.head.prev = None
        return pop_node_data


