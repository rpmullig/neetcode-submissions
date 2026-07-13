class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start: int = 1
        while start**2 < num:
            start +=1 
        
        return start**2 == num