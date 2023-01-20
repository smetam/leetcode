from typing import List


class Solution:

    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        previous = values[0] + values[1] + 0 - 1
        best = previous
        for idx, num in enumerate(values[2:], start=2):
            current = max(values[idx-1] + num - 1, previous - values[idx-1] + num - 1)
            best = max(best, current)
            previous = current
        return best




