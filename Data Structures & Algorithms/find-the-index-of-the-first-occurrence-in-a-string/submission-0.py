class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for left in range(len(haystack)):
            right: int = 0
            while right < len(needle) and right+left < len(haystack) and haystack[left+right] == needle[right]:
                right += 1
            if right == len(needle):
                return left
        
        return -1