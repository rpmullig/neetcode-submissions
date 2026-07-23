class PrefixTree:

    def __init__(self):
        self.data = dict()

    def insert(self, word: str) -> None:
        curr = self.data
        for letter in word:
            if letter in curr:
                curr = curr[letter]
            else:
                curr[letter] = dict()
                curr = curr[letter]
        
        curr["\n"] = None # add ending char
            

    def search(self, word: str) -> bool:
        curr = self.data
        for letter in word:
            if letter not in curr:
                return False
            curr = curr[letter]

        return ("\n" in curr)

    def startsWith(self, prefix: str) -> bool:
        curr = self.data
        for letter in prefix:
            if letter not in curr:
                return False
            curr = curr[letter]

        return True
        