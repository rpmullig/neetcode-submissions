class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums = [elm for elm in nums]
        heapq.heapify(nums)
        self.nums = nums
        self.k = k

        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        return self.nums[0]
