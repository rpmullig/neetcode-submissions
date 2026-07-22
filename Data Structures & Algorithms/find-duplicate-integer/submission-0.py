class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            nums[abs(nums[i]) - 1] *= -1
            i = nums[abs(i) % len(nums)]

        for index in range(len(nums)):
            if nums[index] > 0:
                return nums[index]

        return nums[0]

        