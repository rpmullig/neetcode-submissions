class UnionFind:
    
    def __init__(self, n: int):
        self.data: List[int] = [i for i in range(n)]

    def find(self, x: int) -> int:
        # OPTIMIZATION 1: Path Compression
        # Flattens the tree so future lookups are nearly instant
        if x != self.data[x]:
            self.data[x] = self.find(self.data[x])
        return self.data[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        root_y = self.find(y)
        root_x = self.find(x)

        if root_x == root_y:
            return False

        self.data[root_x] = root_y
        return True

    def getNumComponents(self) -> int:
        output: int = 0 
        for i in range(len(self.data)):
            if i == self.data[i]:
                output += 1
        return output
