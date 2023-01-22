class Solution:
    @staticmethod
    def _get_start(curr: str, end: int) -> int:
        return end if curr in ('1', '2') else 0

    def numDecodings(self, s: str) -> int:
        curr = s[0]
        if curr == '0':
            return 0
        start, end = self._get_start(curr, 1), 1
        
        for prev, curr in zip(s[:-1], s[1:]):
            if curr == '0':
                # current symbol can only be an ending of 2-digit number
                start, end = 0, start
            elif (prev == '1') or (prev == '2' and curr not in ('7', '8', '9')):
                # current symbol can be both one digit number and end of 2-digit number
                start, end = self._get_start(curr, end), start + end 
            else:
                # current symbol is one digit number
                start, end = self._get_start(curr, end), end
        return end

