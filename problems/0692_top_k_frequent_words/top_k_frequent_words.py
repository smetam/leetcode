from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        top_k_frequent = c.most_common()
        top_k_frequent = sorted(top_k_frequent, key=lambda x: (-x[1], x[0]))
        result = []
        for idx, pair in enumerate(top_k_frequent):
            if idx >= k:
                break
            word, _ = pair
            result.append(word)
        return result
