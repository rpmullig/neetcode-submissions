class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output: List[int] = [1] * len(nums)
        left_product: int = 1
        for i in range(len(nums)):
            output[i] *= left_product
            left_product *= nums[i]
        
        right_product: int = 1 
        for i in range(len(nums)-1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]

        return output