from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1

        s_counter = Counter(secret)
        g_counter = Counter(guess)
        for letter, count in s_counter.items():
            cows += min(count, g_counter[letter])
        cows -= bulls
        return f'{bulls}A{cows}B'