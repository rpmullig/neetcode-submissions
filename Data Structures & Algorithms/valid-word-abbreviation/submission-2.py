class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        wordIndex, abbrIndex = 0, 0
        numberSet: Set() = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        while wordIndex < len(word):
            if abbrIndex >= len(abbr):
                return False
            abbreviationElm: str = abbr[abbrIndex]
            if abbreviationElm in numberSet:
                abbrNumber: List[str] = list()
                while abbr[abbrIndex] in numberSet and abbrIndex < len(abbr):
                    abbreviationElm = abbr[abbrIndex]
                    abbrNumber.append(abbreviationElm)
                    abbrIndex += 1
                jumpIndex: int = int("".join(abbrNumber))
                if jumpIndex + wordIndex >= len(word):
                    return False
                wordIndex += jumpIndex
            else:
                if word[wordIndex] != abbr[abbrIndex]:
                    return False
                abbrIndex += 1

            wordIndex += 1
        
        return True

