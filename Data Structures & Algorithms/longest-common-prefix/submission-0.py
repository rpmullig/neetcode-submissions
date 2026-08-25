class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix_index = 0
        prefix = list()
        still_common = True
        while still_common:
            current_letter = None
            for word in strs:
                if current_letter:
                    if prefix_index >= len(word):
                        still_common = False
                        continue
                    
                    if word[prefix_index] != current_letter:
                        still_common = False
                else:
                    current_letter = word[prefix_index]
            
            prefix_index += 1
            if still_common:
                prefix.append(current_letter)


        return ''.join(prefix)