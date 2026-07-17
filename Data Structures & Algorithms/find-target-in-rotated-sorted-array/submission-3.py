class Solution:

    def binary_search(self, nums: List[int], target: int, left: int, right: int) -> int:
        while left <= right: 
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1


    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums) - 1

        while left < right: 

            if nums[left] < nums[right]:
                return self.binary_search(nums, target, left, right)

            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif mid > 0 and nums[mid] > nums[mid -1]:
                if nums[left] <= target and nums[mid] > target:
                    return self.binary_search(nums, target, left, mid - 1)
                else:
                    return self.binary_search(nums, target, mid + 1, right)
            elif nums[mid] < nums[right]: 
                right = mid - 1
            else:
                left  = mid + 1

        return -1 