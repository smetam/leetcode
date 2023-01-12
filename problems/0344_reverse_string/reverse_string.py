from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for idx in range(n // 2):
            s[idx], s[n - 1 - idx] = s[n - 1 - idx], s[idx]
