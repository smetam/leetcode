from typing import List
from functools import lru_cache


class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        dp = [True] + [False for _ in range(n)]

        for i in range(n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break

        return dp[n]


# O(2^n) complexity, time limit problem which can be solved with cache
class Solution1:
    @lru_cache
    def _word_break(self, s: str, words: frozenset[str]) -> bool:
        if s == '':
            return True
        
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if prefix in words:
                if self._word_break(s[i:], words):
                    return True
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = frozenset(wordDict)
        return self._word_break(s, words)
        
