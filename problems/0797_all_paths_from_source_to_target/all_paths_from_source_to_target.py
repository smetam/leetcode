from typing import List
from collections import deque


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n_nodes = len(graph)
        q = deque()
        q.append((0, [0]))
        all_paths = []
        while len(q) > 0:
            current_node, current_path = q.popleft()
            if current_node == n_nodes - 1:
                all_paths.append(current_path)

            connected_nodes = graph[current_node]
            for node in connected_nodes:
                new_path = current_path + [node]
                q.append((node, new_path))
        return all_paths