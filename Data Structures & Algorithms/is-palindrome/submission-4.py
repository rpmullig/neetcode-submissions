class Solution:
    
    def _advance_non_alphanumeric(self, s: str, i: int, increment_step: int) -> int:
        while i >= 0 and i < len(s) and not s[i].isalnum(): # is alpha numeric also can do s[i] in {" ", ", ", ">", "<", "'", ".", ",", ":", ":", "'"}
            i += increment_step
        return i 
    

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        l = self._advance_non_alphanumeric(s, l, 1)
        r = self._advance_non_alphanumeric(s, r, -1)
    
        while l < r and s[l].lower() == s[r].lower():
            l = self._advance_non_alphanumeric(s, l + 1, 1)
            r = self._advance_non_alphanumeric(s, r - 1, -1)
        
        return l >= r