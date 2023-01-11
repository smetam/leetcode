from itertools import count


class Solution:
    @staticmethod
    def find_first_two_mismatch_positions(s1: str, s2: str) -> int:
        mismatches = []
        for i, c1, c2 in zip(count(), s1, s2):
            if c1 != c2:
                mismatches.append(i)
                if len(mismatches) == 3:
                    return mismatches
        return mismatches

    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        mismatches = self.find_first_two_mismatch_positions(s1, s2)
        if len(mismatches) == 0:
            return True
        if len(mismatches) != 2:
            return False
        idx1, idx2 = mismatches
        return (s1[idx1], s1[idx2]) == (s2[idx2], s2[idx1])

