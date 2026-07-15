class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        result: List[int] = []

        window_max_heap: List[int] = list() 
        window_frequency: Dict[int, int] = collections.defaultdict(int)

        for i in range(len(nums)):

            if window_frequency[nums[i]] == 0:
                heapq.heappush(window_max_heap, -nums[i])
            window_frequency[nums[i]] += 1
            
            if i >= k - 1:
                if i >= k: # exteremly tricky indexing. The first window must be filled THEN we need to remove beyond that
                    window_frequency[nums[i - k]] -= 1
                while window_frequency[-window_max_heap[0]] == 0:
                    heapq.heappop(window_max_heap)
                result.append(-window_max_heap[0])

    
        return result