class Deque:

    class Node:
        def __init__(self, prev_node: 'Deque.Node', data: int, next_node: 'Deque.Node'):
            self.data = data
            self.next_node = next_node
            self.prev_node = prev_node

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self) -> bool:
        return self.size == 0

    def append(self, value: int) -> None:
        new_node = Deque.Node(self.tail, value, None)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
        self.size += 1

    def appendleft(self, value: int) -> None:
        new_node = Deque.Node(None, value, self.head)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            self.head.prev_node = new_node
            self.head = new_node
        self.size += 1

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        pop_node = self.tail
        self.tail = self.tail.prev_node
        if self.tail:
            self.tail.next_node = None
        else:
            self.head = None
        self.size -= 1
        return pop_node.data

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        pop_node = self.head
        self.head = self.head.next_node
        if self.head:
            self.head.prev_node = None
        else:
            self.tail = None
        self.size -= 1
        return pop_node.data
