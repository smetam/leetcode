from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for idx, c in enumerate(s):
            if counter[c] == 1:
                return idx
        return -1
