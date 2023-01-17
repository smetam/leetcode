from typing import List


class Solution:
    @staticmethod
    def sort_key(num: int):
        num_one_bits = sum(map(int, bin(num)[2:]))
        # sort by number of bits first, then by number
        return num_one_bits, num

    def sortByBits(self, arr: List[int]) -> List[int]:
        return list(sorted(arr, key=self.sort_key))