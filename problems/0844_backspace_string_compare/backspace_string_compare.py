class Solution:
    @staticmethod
    def _decode(seq: str) -> str:
        stack = list()
        for sym in seq:
            if sym == '#' and len(stack) > 0:
                stack.pop()
            if sym.isalpha():
                stack.append(sym)
        return ''.join(stack)

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self._decode(s) == self._decode(t)
