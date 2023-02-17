from typing import List
from collections import deque


class Solution:
    @staticmethod
    def distance(left: str, right: str) -> int:
        dist = 0
        for l, r in zip(left, right):
            dist += l != r
        return dist

    def build_adj_matrix(self, bank):
        adj = {gene: [] for gene in bank}
        for left in bank:
            for right in bank:
                if self.distance(left, right) == 1:
                    adj[left].append(right)
        return adj


    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1

        if startGene not in bank:
            bank.append(startGene)

        adj = self.build_adj_matrix(bank)

        visited = set()
        q = deque()

        visited.add(startGene)
        q.append((startGene, 0))
        while len(q) > 0:
            gene, steps = q.popleft()
            if gene == endGene:
                return steps
            
            for mutation in adj[gene]:
                if mutation in visited:
                    continue
                visited.add(mutation)
                q.append((mutation, steps + 1))
        return -1
