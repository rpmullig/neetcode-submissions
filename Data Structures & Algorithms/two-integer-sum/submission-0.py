class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        inverseLookup: Dict[int, int] = dict()
        for i, num in enumerate(nums):
            inverseLookup[target - num] = i
        for i, num in enumerate(nums):
            if num in inverseLookup and inverseLookup[num] != i:
                return [i, inverseLookup[num]]
        return -1 