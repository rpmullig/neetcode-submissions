class Solution:

    def encode(self, strs: List[str]) -> str:
        result: List[str] = list()
        for word in strs:
            result.append(str(len(word)))
            result.append('|_|')
            result.append(word)
        return ''.join(result)

    def decode(self, s: str) -> List[str]:
        result: List[str] = list()
        l, r = 0, 0
        while l < len(s):
            r = l
            while s[r] != '|' and r < len(s):
                r += 1
            word_length: int = int(s[l:r])
            result.append(s[r+3:r+3+word_length])
            l = r + 3 + word_length 

        return result