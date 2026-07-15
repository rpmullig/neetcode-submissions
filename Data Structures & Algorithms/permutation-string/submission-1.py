class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        primary_letter_counts = collections.defaultdict(int)
        for letter in s1:
            primary_letter_counts[letter] += 1

        current_window = collections.defaultdict(int)
        left = 0 
        for right in range(len(s2)):
            current_window[s2[right]] += 1
            while left <= right and current_window[s2[right]] > primary_letter_counts[s2[right]]:
                current_window[s2[left]] -= 1
                left += 1
            
            if (right - left + 1) == len(s1):
                return True
        
        return False
