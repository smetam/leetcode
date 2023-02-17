from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        edge_set = set(range(n))
        for _, edge_to in edges:
            edge_set.discard(edge_to)
        return edge_set
