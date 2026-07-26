class Solution:


    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)

            if x < y:
                y = (y - x)
                heapq.heappush(stones, -y)


        if len(stones) == 1:
            return -stones[0]
        else:
            return 0