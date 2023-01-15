class Solution:
    @staticmethod
    def _convert(sym: str) -> str:
        return chr(ord('a') - 1 + int(sym))

    def freqAlphabets(self, s: str) -> str:
        res = []
        idx = len(s) - 1
        while idx >= 0:
            sym = s[idx]
            if sym == '#':
                sym = s[idx-2:idx]
                idx -= 3
            else:
                idx -= 1
            res.append(self._convert(sym))
        return ''.join(reversed(res))