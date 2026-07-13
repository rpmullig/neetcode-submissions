class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "[empty]"
        return '|+|'.join(strs)

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return [""]
        elif len(s) == 1:
            return [s]
        elif s == "[empty]":
            return []
        return s.split('|+|')