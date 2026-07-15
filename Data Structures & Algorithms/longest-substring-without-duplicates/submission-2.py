class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window: Set[str] = set()
        max_diff: int = 0
        left, right = 0, 0 
        while right < len(s):
            while left != right and s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            right += 1
            max_diff = max(max_diff, right - left)


    
        return max_diff