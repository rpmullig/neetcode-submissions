class Solution:

    def encode(self, strs: List[str]) -> str:
        return '|+|'.join(strs)

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return [""]
        return s.split('|+|')