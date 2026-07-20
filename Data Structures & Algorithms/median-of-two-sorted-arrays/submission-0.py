class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n, m = len(nums1), len(nums2)
        half = (m + n) // 2

        left, right = 0, n
        while left <= right:
            mid_1 = (left + right) // 2
            mid_2 = half - mid_1

            l1 = nums1[mid_1 - 1] if mid_1 > 0 else -math.inf
            r1 = nums1[mid_1] if mid_1 < n else math.inf

            l2 = nums2[mid_2 - 1] if mid_2 > 0 else -math.inf
            r2 = nums2[mid_2] if mid_2 < m else math.inf

            if l1 <= r2 and l2 <= r1:
                if (n + m) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return min(r1, r2)
            elif l1 > r2:
                right = mid_1 - 1
            else:
                left = mid_1 + 1


        return -1 