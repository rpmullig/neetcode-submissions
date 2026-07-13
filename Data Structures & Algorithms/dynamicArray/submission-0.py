class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity: int = capacity 
        self.length: int = 0
        self.data: [int] = [None for _ in range(self.capacity)]


    def get(self, i: int) -> int:
        return self.data[i]


    def set(self, i: int, n: int) -> None:
        self.data[i] = n


    def pushback(self, n: int) -> None:
        if self.capacity == self.length:
            self.resize()
        self.data[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1
        return self.data[self.length]
 

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity 
        
        for i in range(self.length):
            new_arr[i] = self.data[i]
        self.data = new_arr

    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity
