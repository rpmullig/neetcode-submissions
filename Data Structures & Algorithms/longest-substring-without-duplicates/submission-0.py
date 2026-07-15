class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen: Set[str] = set()
        max_diff: int = 0
        left, right = 0, 0 
        while right < len(s):
            while right < len(s) and s[right] not in seen:
                seen.add(s[right])
                right += 1
                max_diff = max(max_diff, right - left)
            seen.clear()
            left = right

        return max_diff