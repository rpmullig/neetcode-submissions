class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        seenNumbers: List[int] = [0 for _ in range(255)]
        for letter in s:
            seenNumbers[ord(letter)] += 1
    
        for letter in t:
            if seenNumbers[ord(letter)] == 0:
                return False
            else:
                seenNumbers[ord(letter)] -= 1


        return sum(seenNumbers) == 0 