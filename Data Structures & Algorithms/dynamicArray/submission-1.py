class DynamicArray:
    
    def __init__(self, capacity: int):
        assert capacity > 0 
        self.data: List[int] = [None for _ in range(capacity)]
        self.capacity: int = capacity
        self.size: int = 0

    def get(self, i: int) -> int:
        assert i < self.getCapacity() and i >= 0
        return self.data[i]

    def set(self, i: int, n: int) -> None:
        assert i < self.getCapacity() and i >= 0 and i < self.size
        self.data[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() == self.getCapacity():
            self.resize()
        self.data[self.size] = n
        self.size += 1

    def popback(self) -> int:
        assert self.size > 0
        elm: int = self.data[self.size - 1] 
        self.data[self.size - 1] = None
        self.size -= 1
        return elm

    def resize(self) -> None:
        self.capacity *= 2
        newArr: List[int] = [None for _ in range(self.capacity)]
        for i, elm in enumerate(self.data):
            newArr[i] = elm
        self.data = newArr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity