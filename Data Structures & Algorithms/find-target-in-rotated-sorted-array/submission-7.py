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
        
        assert len(nums) > 0

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1


        left, right = 0, len(nums) - 1

        while left <= right: 

            if nums[left] <= nums[right]:
                return self.binary_search(nums, target, left, right)

            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    return self.binary_search(nums, target, left, mid - 1)
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    return self.binary_search(nums, target, mid + 1, right)
                else:
                    right = mid - 1

        return -1 