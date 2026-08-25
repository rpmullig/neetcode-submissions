class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] == val:
                while left <= right and nums[right] == val:
                    right -= 1 
                
                if left < right:
                    nums[left] = nums[right]
                    nums[right] = val
                    right -= 1
                else:
                    break
            
            left += 1

        return right + 1