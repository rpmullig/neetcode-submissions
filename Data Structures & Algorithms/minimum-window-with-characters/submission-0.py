class Solution:
    def minWindow(self, s: str, t: str) -> str:

        min_window: int = len(s) + 1
        valid_substrings: Dict[int, List[int]] = dict() 

        t_character_frequencies = collections.defaultdict(int)
        for letter in t:
            t_character_frequencies[letter] += 1
        
        window_frequencies = collections.defaultdict(int)
        left: int = 0 
        required_chars: int = len(t_character_frequencies) # just the characters we need
        formed_chars: int = 0

        for right in range(len(s)):
            letter: str = s[right]
            window_frequencies[letter] += 1
            
            if letter in t_character_frequencies and window_frequencies[letter] == t_character_frequencies[letter]:
                formed_chars += 1

            while formed_chars == required_chars:
                if (right - left + 1) < min_window:
                    min_window = (right - left + 1)
                    valid_substrings[min_window] = [left, right]
                
                left_letter = s[left]
                window_frequencies[left_letter] -= 1
                if left_letter in t_character_frequencies and window_frequencies[left_letter] < t_character_frequencies[left_letter]:
                    formed_chars -= 1
                left += 1 

        if len(valid_substrings) == 0:
            return ""

        result_index = valid_substrings[min_window] 
        result: List[str] = [s[i] for i in range(result_index[0], result_index[1] + 1, 1)]
        return ''.join(result)
