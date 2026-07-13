class Solution:

    def _isNumber(self, char: str) -> bool:
        numberSet: Set() = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        return char in numberSet

    def _extractNumber(self, abbr:str, index: int):
        abbrNumber: List[str] = list()
        abbreviationElm: str = abbr[index]

        if abbreviationElm == "0":
            return (math.inf, math.inf)

        while index < len(abbr) and self._isNumber(abbr[index]):
            abbreviationElm = abbr[index]
            abbrNumber.append(abbreviationElm)
            index += 1
        return (int("".join(abbrNumber)), index)


    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        wordIndex, abbrIndex = 0, 0
        while wordIndex < len(word) and abbrIndex < len(abbr):
            abbreviationElm: str = abbr[abbrIndex]
            if self._isNumber(abbreviationElm):
                jumpIndex, abbrIndex = self._extractNumber(abbr, abbrIndex)
                if jumpIndex + wordIndex > len(word): # did it exceed the word? 
                    return False
                wordIndex += jumpIndex
            else:
                if word[wordIndex] != abbreviationElm:
                    return False
                abbrIndex += 1
                wordIndex += 1
        
        return abbrIndex == len(abbr) and wordIndex == len(word)