class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.maxNumbers: int = maxNumbers
        self.usedNumbers: Set[int] = set()
        self.freeNumbers: Set[int] = set()
        for i in range(self.maxNumbers):
            self.freeNumbers.add(i)

    def get(self) -> int:
        if len(self.freeNumbers) == 0:
            return -1
        result: int = self.freeNumbers.pop()
        self.usedNumbers.add(result)
        return result

    def check(self, number: int) -> bool:
        return number in self.freeNumbers

    def release(self, number: int) -> None:
        self.usedNumbers.discard(number)
        self.freeNumbers.add(number)
        return None


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
