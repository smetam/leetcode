from collections import Counter

# O(len(s1) + len(S2))
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        counter = Counter(s1)
        s_counter = Counter(s2[:n])
        if counter == s_counter:
            return True
        for sym_drop, sym_add in zip(s2[:-n], s2[n:]):
            s_counter[sym_drop] -= 1
            if s_counter[sym_drop] == 0:
                del s_counter[sym_drop]
            s_counter[sym_add] += 1
            if counter == s_counter:
                return True
        return False


# O(len(s1) * len(S2))
class Solution2:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        counter = Counter(s1)
        for i in range(len(s2) - n + 1):
            s = s2[i:i+n]
            s_counter = Counter(s)
            if counter == s_counter:
                return True
        return False