# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int, guess) -> int:
        low = 1
        high = n
        num = (low+high) // 2
        res = guess(num)
        while res != 0:
            print(num, low, high)
            if res == -1:
                high = num - 1
            else:
                low = num + 1
            num = (low+high) // 2
            res = guess(num)
        return num
