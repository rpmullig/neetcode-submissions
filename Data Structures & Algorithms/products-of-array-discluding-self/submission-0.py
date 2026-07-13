class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product: List[int] = [1] * len(nums)
        for i in range(len(nums)):
            if i > 0:
                left_product[i] = (left_product[i-1] * nums[i-1])
        
        print(left_product)
        right_product: List[int] = [1] * len(nums)
        for i in range(len(nums), -1, -1):
            if i < len(nums) - 1:
                right_product[i] = right_product[i+1] * nums[i+1]

        print(right_product)

        return [right_product[i] * left_product[i] for i in range(len(nums))]