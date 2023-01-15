class Solution:
    def toLowerCase(self, s: str) -> str:
        # solution with "lower"
        # return s.lower()
        res = []
        diff = ord('a') - ord('A')
        for sym in s:
            sym_ord = ord(sym)
            if ord('A') <= sym_ord <= ord('Z'):
                sym_ord += diff
            res.append(chr(sym_ord))
        return ''.join(res)