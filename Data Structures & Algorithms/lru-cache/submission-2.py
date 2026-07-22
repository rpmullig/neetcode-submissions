class LRUCache:

    class ListNode:
        def __init__(self, value, key, next = None, prev = None):
            self.value = value
            self.key = key
            self.next = next
            self.prev = prev
        
        def __hash__(self):
            return hash(self.key)

    def _update(self, node) -> int:
        if node == self.head:
            return node.value
        
        if node == self.tail:
            self.tail = node.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            
        node.next = self.head
        node.prev = None
        self.head.prev = node
        self.head = node
                
        return node.value

    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.length = 0
        self.map = dict() 
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.map:
            return self._update(self.map[key])
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.value = value
            self._update(node)  
            return None             
        
        if self.length == self.capacity:
            evict = self.tail
            self.map.pop(evict.key, None)
            
            if evict.prev: 
                self.tail = evict.prev
                self.tail.next = None
            else: 
                self.head = None
                self.tail = None
                
            self.length -= 1 
            
        new_node = self.ListNode(value, key)
        self.map[key] = new_node
        
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
        self.length += 1
        