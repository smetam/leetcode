from typing import List


class Solution:
    @classmethod
    def _permute(cls, indices: set) -> List[List[int]]:
        if len(indices) == 0:
            return [[]]
        permutations = []
        for idx in indices:
            for tail in cls._permute(indices - {idx}):
                permutations.append([idx] + tail)
        return permutations

    def permute(self, nums: List[int]) -> List[List[int]]:
        indices = set(range(len(nums)))
        idx_permutations = self._permute(indices)
        res = []
        for perm in idx_permutations:
            res.append(list(map(lambda x: nums[x], perm)))
        return res
        