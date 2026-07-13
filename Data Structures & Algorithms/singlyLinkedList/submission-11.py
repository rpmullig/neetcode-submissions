class LinkedList:
    class Node:
        def __init__(self, val=None):
            self.val = val
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or self.length <= index or self.length == 0:
            return -1
        current = self.head
        i = 0
        while i < index:
            current = current.next
            i += 1

        return current.val

    def insertHead(self, val: int) -> None:
        if self.length == 0:
            self.head = self.Node(val=val)
            self.tail = self.head
            self.length = 1
            return None

        new_node = self.Node(val=val)
        new_node.next = self.head
        self.head = new_node
        self.length += 1 


    def insertTail(self, val: int) -> None:
        if self.length == 0:
            self.head = self.Node(val=val)
            self.tail = self.head
            self.length = 1
            return None

        self.tail.next = self.Node(val=val)
        self.tail = self.tail.next
        self.length += 1

    def remove(self, index: int) -> bool:

        if index < 0 or index >= self.length or self.length == 0:
            return False
    
        if self.length == 1:
            self.head = None
            self.tail = None
            return True

        if index == 0:
            self.head = self.head.next

        current = self.head
        for i in range(index - 1):
            current = current.next
        current.next = current.next.next
        if self.length == index + 1: # update tail
            self.tail = current
        self.length -= 1
        return True


    def getValues(self) -> List[int]:
        current = self.head
        result: List[int] = list()
        while current:
            result.append(current.val)
            current = current.next
        
        return result
        
