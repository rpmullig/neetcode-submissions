class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) > h:
            return -1 

        left, right = 1, max(piles)

        k: int = right 

        while left <= right: 
            mid = left + ((right - left) // 2)
            current_time: int = 0
            for elm in piles:
                current_time += math.ceil(elm / mid)
            
            if current_time <= h:
                k = mid
                right = mid - 1
            else:
                left = mid + 1

        return k