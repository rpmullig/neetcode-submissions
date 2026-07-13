class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted_elements: Dict[int: int] = collections.defaultdict(int)
        for elm in nums:
            counted_elements[elm] += 1

        frequencies = sorted(counted_elements.values(), key=lambda x: -x)[:k]
        result: List[int] = list()
        for key, value in counted_elements.items():
            if value in frequencies:
                result.append(key)


        return result