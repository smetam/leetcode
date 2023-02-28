from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        c = Counter()
        n = len(s)
        left = 0
        for right in range(n):
            letter = s[right]
            c[letter] += 1
            _, count = c.most_common(1)[0]
            required_replacements = right - left - count + 1
            if required_replacements > k:
                letter = s[left]
                c[letter] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
