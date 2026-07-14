class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_consecutive: int = 0
        num_set: Set[int] = set(nums)
        for num in nums:
            if num - 1 not in num_set:  # this makes it O(n) :p
                current_consecutive: int = 1
                current_num: int = num + 1 
                while current_num in num_set:
                    current_consecutive += 1
                    current_num += 1
                longest_consecutive = max(longest_consecutive, current_consecutive)

        return longest_consecutive



