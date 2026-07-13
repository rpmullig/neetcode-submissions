class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        rightSum, leftSum = sum(nums), 0 # O(n) time, O(1) space

        for i, elm in enumerate(nums): # O(n) time, O(1) space
            rightSum -= elm
            if leftSum == rightSum:
                return i

            leftSum += elm

        return -1 

        # Start: leftSum: 0 rightSum: 28
        # 0 | lefSum: 0 rightSum: 27
        # 1 | leftSum: 8 rightSum: 20
        # 2 | leftSum: 11 rightSmm: 17
        # 3 | lftSum: 16 rightSum: 11
