class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbersSeen: Set[int] = set()
        for num in nums:
            if num in numbersSeen:
                return True
            numbersSeen.add(num)
        return False