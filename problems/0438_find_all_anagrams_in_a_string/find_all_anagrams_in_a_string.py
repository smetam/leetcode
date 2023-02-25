from typing import List
from collections import Counter
from itertools import count


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        n = len(p)
        
        if n > len(s):
            return result

        p_counter = Counter(p)
        s_counter = Counter(s[:n])
        if p_counter == s_counter:
            result.append(0)
        
        for idx, out_c, in_c in zip(count(1), s[:-n], s[n:]):
            s_counter[out_c] -= 1
            s_counter[in_c] += 1
            # unary + is needed to remove all zeroes
            if p_counter == (+s_counter):
                result.append(idx)

        return result
