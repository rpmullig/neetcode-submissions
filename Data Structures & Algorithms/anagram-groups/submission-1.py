class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = collections.defaultdict(list)
        for word in strs:
            groupings[''.join(sorted(word))].append(word)
        
        return list(groupings.values())