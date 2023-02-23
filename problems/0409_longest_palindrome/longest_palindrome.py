from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        max_len = 0
        c = Counter(s)
        single = False
        for _, count in c.items():
            is_odd = count % 2 == 1
            single = single or is_odd
            max_len += count - 1 if is_odd else count
        return max_len + single
