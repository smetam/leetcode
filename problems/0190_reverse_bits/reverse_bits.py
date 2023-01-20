from functools import reduce


class Solution:
    def reverseBits(self, n: int) -> int:
        # take bin representation without prefix '0b'
        n = bin(n)[2:]
        
        # add leading zeros up to 32 bits and reverse
        seq = reversed(n.zfill(32))

        # compute new number
        return reduce(lambda acc, b: acc << 1 | int(b), seq, 0)