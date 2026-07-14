class UnionFind:
    
    def __init__(self, n: int):
        self.data: List[int] = [i for i in range(n)]

    def find(self, x: int) -> int:
        while x != self.data[x]:
            x = self.data[x]
        return x

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.data[self.find(x)] == self.data[self.find(y)]

    def union(self, x: int, y: int) -> bool:
        if self.isSameComponent(x,y):
            return False
        self.data[y] = self.find(x)
        return True

    def getNumComponents(self) -> int:
        return len(set(self.data))
