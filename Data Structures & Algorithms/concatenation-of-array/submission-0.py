class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n: int = len(nums)
        for i in range(n):
            nums.append(nums[i])
        return nums
        