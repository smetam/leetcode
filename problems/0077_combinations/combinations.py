from typing import List


class Solution:
    @classmethod
    def _combine(cls, start: int, end: int, k: int) -> List[List[int]]:
        if k == 0:
            return [[]]
        comb = []
        for i in range(start, end + 1 - (k - 1)):
            for tail in cls._combine(i+1, end, k-1):
                elem = [i] + tail
                comb.append(elem)
        return comb

    def combine(self, n: int, k: int) -> List[List[int]]:
        return self._combine(1, n, k)
