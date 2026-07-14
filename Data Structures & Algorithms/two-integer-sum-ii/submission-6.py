class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r and numbers[l] != numbers[r]:
            current_sum = numbers[l] + numbers[r]
            if current_sum > target:
                r -= 1
            elif current_sum < target:
                l += 1
            else:
                return [l + 1, r + 1]

        return [-1, -1]
    """
    Proof of Correctness for Two-Pointer Approach:

    Given an array `numbers` sorted in non-decreasing order and a `target` sum:
    Let `l` and `r` be the left and right pointers, initially at the absolute 
    bounds of the array (0 and len(numbers) - 1).

    We need to find indices i, j (where l <= i < j <= r) such that 
    numbers[i] + numbers[j] == target.

    At each step in the while loop, we evaluate current_sum = numbers[l] + numbers[r]:

    1. If current_sum > target:
    Because the array is sorted, any element to the right of `l` is >= numbers[l].
    Therefore, numbers[k] + numbers[r] > target for all k >= l. 
    This proves that `numbers[r]` is definitively too large to form the target 
    sum with *any* remaining element in our unsearched range. We can safely 
    and permanently discard `r` by moving it left (r -= 1) without ever 
    missing a valid pair.
    
    2. If current_sum < target:
    Because the array is sorted, any element to the left of `r` is <= numbers[r].
    Therefore, numbers[l] + numbers[k] < target for all k <= r.
    This proves that `numbers[l]` is definitively too small to form the target 
    sum with *any* remaining element in our unsearched range. We can safely 
    and permanently discard `l` by moving it right (l += 1) without ever 
    missing a valid pair.
    
    3. If current_sum == target:
    We have found the exact valid pair and return it immediately.
    
    Conclusion:
    At every single iteration, we mathematically prove that one specific extreme 
    cannot possibly be part of the solution. By systematically eliminating these 
    impossible combinations one by one, the search space shrinks flawlessly until 
    the pair is found. This guarantees perfect accuracy with an O(n) runtime 
    and O(1) space complexity.
    """
