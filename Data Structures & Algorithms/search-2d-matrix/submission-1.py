class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        assert len(matrix) > 0
        n = len(matrix[0])

        left, right = 0, m - 1
        i = 0
        while left <= right:
            mid = left + ((right - left) // 2)
            row = matrix[mid]
            start, end = row[0], row[len(row) - 1]
            if start <= target and end >= target:
                i = mid
                break
            elif start > target:
                right = mid - 1
            else:
                left = mid + 1
        

        left, right = 0, n - 1
        search_row = matrix[i]
        while left <= right:
            mid = left + ((right - left) // 2)
            if search_row[mid] == target:
                return True
            elif search_row[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        

        return False