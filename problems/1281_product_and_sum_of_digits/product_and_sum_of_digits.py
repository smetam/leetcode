from functools import reduce
import operator

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(digit) for digit in str(n)]
        digit_product = reduce(operator.mul, digits)
        digit_sum = sum(digits)
        return digit_product - digit_sum