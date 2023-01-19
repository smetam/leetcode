from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        if len(s) == 1:
            return {s.lower(), s.upper()}
        permutations = []
        for c in {s[0].lower(), s[0].upper()}:
            for tail in self.letterCasePermutation(s[1:]):
                permutations.append(c + tail)
        return permutations
            
