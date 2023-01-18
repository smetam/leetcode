from typing import List


# O(m + n) solution
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        max_dist = 0
        i, j = 0, 0
        while (i < n) and (j < m):
            if nums1[i] > nums2[j]:
                i += 1
            else:
                max_dist = max(max_dist, j - i)
                j += 1
        return max_dist


# O(n * log m) solution, does not take into account that nums1 is sorted
class Solution1:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        max_dist = 0
        for idx, num in enumerate(nums1):
            left, right = idx, len(nums2) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums2[mid] < num:
                    right = mid - 1
                else:
                    left = mid + 1
            max_dist = max(max_dist, right-idx)
        return max_dist
