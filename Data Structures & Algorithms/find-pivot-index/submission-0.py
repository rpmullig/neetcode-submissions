class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        leftCummulativeSum: List[int] = [0]
        for i in range(len(nums)): # enumerate? 
            elm: int = nums[i]
            leftCummulativeSum.append(leftCummulativeSum[-1] + elm)
        
        leftCummulativeSum.pop(0) # remove the 0 starter for clean loop
        print(leftCummulativeSum)
        currentRightCummulativeSum: int = 0
        for i in reversed(range(len(nums))): # cleaner?
            currentRightCummulativeSum += nums[i]
            if currentRightCummulativeSum == leftCummulativeSum[i]:
                return i
        
        return -1