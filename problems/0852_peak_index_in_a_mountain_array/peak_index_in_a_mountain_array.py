from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        start = 0
        end = n - 1
        while (end - start) > 2:
            one_third = (end - start) // 3
            left = start + one_third
            right = left + one_third
            if arr[left] > arr[right]:
                end = right
            else:
                start = left

        peak_zone = arr[start: end + 1]
        peak = 0
        peak_idx = 0
        for idx, value in enumerate(peak_zone):
            if  value > peak:
                peak = value
                peak_idx = idx
        return start + peak_idx