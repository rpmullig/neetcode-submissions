class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        return self.nums[-self.k]
