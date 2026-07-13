class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        container: Dict[str: List[int]] = dict()
        for i, word in enumerate(strs):
            split_word: List[str] = list()
            for letter in word:
                split_word.append(letter)
            split_word.sort()
            sorted_str: str = ''.join(split_word)
            print(sorted_str)
            if sorted_str in container:
                container[sorted_str].append(i)
            else:
                container[sorted_str] = [i]
        
        result: List[List[str]] = list()
        for anagram in container.keys():
            new_group: List[str] = list()
            for i in container[anagram]:
                new_group.append(strs[i])
            result.append(new_group)
        
        return result