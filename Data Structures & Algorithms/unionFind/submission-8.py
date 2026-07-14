from typing import List

class UnionFind:
    
    def __init__(self, n: int):
        self.data: List[int] = [i for i in range(n)]
        # Track sizes to prevent the tree from ever getting too deep
        self.size: List[int] = [1] * n

    def find(self, x: int) -> int:
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

        # --- THE UNOPTIMIZED WAY (Causes RecursionError in deep graphs) ---
        # self.data[root_x] = root_y
        # ------------------------------------------------------------------

        # --- THE OPTIMIZED WAY (Union by Size) ---
        if self.size[root_x] < self.size[root_y]:
            self.data[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.data[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            
        return True

    def getNumComponents(self) -> int:
        output: int = 0 
        for i in range(len(self.data)):
            if i == self.data[i]:
                output += 1
        return output