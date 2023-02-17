from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        judge_candidate = set(range(1, n + 1))
        trusted_by = {i: 0 for i in range(1, n + 1)}
        for left, right in trust:
            # left cant be judge, since judge does not trust anyone
            judge_candidate.discard(left)
            trusted_by[right] += 1

        print(judge_candidate)
        print(trusted_by)

        if len(judge_candidate) != 1:
            return -1

        candidate = judge_candidate.pop()
        if trusted_by[candidate] == n - 1:
            return candidate
        return -1
