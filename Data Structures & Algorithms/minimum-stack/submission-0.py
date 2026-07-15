class MinStack:

    def __init__(self):
        self.n = 0
        self.data = []
        self.mins = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if self.n > 0:
            self.mins.append(min(self.mins[-1], val))
        else:
            self.mins.append(val)
        self.n += 1

    def pop(self) -> None:
        self.data.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        if self.n == 0:
            return -math.inf

        return self.mins[-1]