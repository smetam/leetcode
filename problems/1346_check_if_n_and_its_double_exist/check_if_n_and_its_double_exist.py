from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for elem in arr:
            half, even, double = elem // 2, elem % 2 == 0, elem * 2
            if double in seen or (even and half in seen):
                return True
            seen.add(elem)
        return False
