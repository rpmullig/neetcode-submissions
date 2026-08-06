class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
         
        class coord:
            def __init__(self, x, y):
                self.x = x
                self.y = y
                self.euclidean_dist = math.sqrt(math.pow(x, 2) + math.pow(y,2))

            def __lt__(self, other):
                return self.euclidean_dist < other.euclidean_dist


        
        points = [coord(point[0], point[1]) for point in points]
        heapq.heapify(points)
    
        result = list() 
        i = 0 
        while i < k:
            i += 1
            coord = heapq.heappop(points)
            result.append([coord.x, coord.y])

        return result 