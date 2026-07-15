class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen: Dict[str: int] = collections.defaultdict(int)
        max_diff, left = 0, 0
        max_frequency: int = 0 

        for right in range(len(s)):
            seen[s[right]] += 1

            while ((right - left + 1) - max(seen.values())) > k: 
                seen[s[left]] -= 1
                left += 1
        
            max_diff = max(max_diff, right - left + 1)
        
        return max_diff