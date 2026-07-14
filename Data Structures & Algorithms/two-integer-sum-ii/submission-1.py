class Solution:
    def _binary_search(self, numbers:List[int], left: int, right: int, target) -> int:
        while left <= right:
            mid: int = left + ((right - left) // 2)
            print(f'mid: {mid} | left: {left} | right: {right}')
            if numbers[mid] == target:
                return mid
            elif numbers[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1

    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i: int = 0 
        while i < len(numbers) - 1:
            if numbers[i] == numbers[i+1]:
                i += 1
                continue
            target_index: int = self._binary_search(numbers, i+1, len(numbers) - 1, target - numbers[i])
            if target_index != -1:
                return [i+1, target_index+1]
            i += 1
        
            
        return [-1, -1]