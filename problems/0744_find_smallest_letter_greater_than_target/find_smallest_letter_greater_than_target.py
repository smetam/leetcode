from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        while left <= right:
            mid = (left + right) // 2
            letter = letters[mid]
            if letter <= target:
                left = mid + 1
            else: 
                right = mid - 1
        if left >= len(letters):
            return letters[0]
        return letters[left]