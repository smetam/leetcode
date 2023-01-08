from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx1, idx2 = m - 1, n - 1
        idx = m + n - 1
        while idx2 >= 0:
            if idx1 < 0:
                for i in range(idx2+1):
                    nums1[i] = nums2[i]
                return nums1
        
            n1 = nums1[idx1]
            n2 = nums2[idx2]
            if n1 <= n2:
                nums1[idx] = n2
                idx2 -= 1
            else:
                nums1[idx] = n1
                idx1 -= 1
            idx -= 1

        # Uncomment this to run tests
        # return nums1
