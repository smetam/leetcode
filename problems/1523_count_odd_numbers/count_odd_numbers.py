class Solution:
    def countOdds(self, low: int, high: int) -> int:
        n_ints = high + 1 - low
        # if interval lenght is even, than half of the interval numbers are odd
        if n_ints % 2 == 0:
            return n_ints // 2
        # if interval lenght is odd, than check first element
        if low % 2 == 0:
            return n_ints // 2
        return n_ints // 2 + 1

