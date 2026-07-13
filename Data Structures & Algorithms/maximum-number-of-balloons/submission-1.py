class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        textLetterCount: Dict[chr: int] = dict()
        baloonLetterCount: Dict[chr: int] = dict()
        for letter in "balloon":
            if letter not in baloonLetterCount:
                baloonLetterCount[letter] = 1
                textLetterCount[letter] = 0 
            else:
                baloonLetterCount[letter] += 1

        for letter in text:
            if letter in baloonLetterCount:
                textLetterCount[letter] += 1

        maxWords: int = math.inf
        for letter in baloonLetterCount.keys():
            countInBaloon: int = baloonLetterCount[letter]
            countInText: int = textLetterCount[letter]
            maxWords = min(maxWords, countInText // countInBaloon)

        return maxWords