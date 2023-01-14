from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = Counter(s)
        t = Counter(t)
        key, _ = (t-s).most_common(1)[0]
        return key