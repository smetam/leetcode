class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        for w1, w2 in zip(word1, word2):
            result.extend((w1, w2))
        n = min(len(word1), len(word2))
        result = ''.join(result) + word1[n:] + word2[n:]
        return result