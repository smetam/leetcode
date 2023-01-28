class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a = a.zfill(n)
        b = b.zfill(n)
        carry = 0
        res = []
        for x, y in zip(reversed(a), reversed(b)):
            add = int(x) + int(y) + carry
            curr, carry = add % 2, add // 2
            res.append(curr)
        if carry:
            res.append(carry)
        return ''.join(map(str, reversed(res)))