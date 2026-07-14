class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_numbers = dict()
        for i, num in enumerate(nums):
            unique_numbers[num] = i


        unions: List[int] = [i for i in range(len(nums))]
        sizes: List[int] = [1 for i in range(len(nums))]

        def find(x):
            while x != unions[x]:
                x = unions[x]
            return x

        def union(x, y):
            if find(x) == find(y):
                return False

            root_x = find(x)
            root_y = find(y)

            if sizes[root_x] > sizes[root_y]:
                sizes[root_x] += sizes[root_y]
                unions[root_y]  = root_x
            else:
                sizes[root_y] += sizes[root_x]
                unions[root_x]  = root_y
                        
            return True 
        
        for num in nums:
            if num - 1 in unique_numbers:
                union(unique_numbers[num], unique_numbers[num-1])
        
        return max(sizes)



