class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0

        n = len(nums) 
        left, right = 0, n - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[left] > nums[mid]:
                right = mid - 1
            else: 
                left = mid + 1

  
        return nums[left]