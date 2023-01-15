from typing import List
from itertools import count


class Solution:
    @staticmethod
    def is_sorted(word1: str, word2: str, order: dict) -> bool:
        for sym1, sym2 in zip(word1, word2):
            if order[sym1] < order[sym2]:
                return True
            elif order[sym1] > order[sym2]:
                return False
            # if equal, go to next char
        return True
        
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # space ' ' marks end of the word
        order = dict(zip(' ' + order, count()))
        for word1, word2 in zip(words[:-1], words[1:]):
            if not self.is_sorted(word1 + ' ', word2 + ' ', order):
                return False
        return True
