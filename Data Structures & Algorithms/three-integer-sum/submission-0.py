class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i: int = 0
        triplets_seen: Set[Tuple] = set() 
        nums.sort()
        output: List[List[int]] = list() 
        while i < len(nums):
            target: int = 0 - nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target and (nums[i], nums[l], nums[r]) not in triplets_seen:
                    triplets_seen.add((nums[i], nums[l], nums[r]))
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                if nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
            i += 1
        return output 