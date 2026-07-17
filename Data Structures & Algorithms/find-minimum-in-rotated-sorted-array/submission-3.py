class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        n = len(nums) 
        left, right = 0, n - 1

        while left < right:
            # If the range is already sorted, the leftmost is the minimum
            if nums[left] < nums[right]:
                return nums[left]

            mid = left + (right - left) // 2
            
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[left] < nums[mid] and nums[mid] < nums[right]:
                right = mid
            else: 
                left = mid 


        return nums[left]