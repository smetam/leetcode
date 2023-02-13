from typing import List
from collections import deque


class Solution:
    
    @staticmethod
    def positive_min(pair):
        left, right = pair
        if left == -1:
            return right
        if right == -1:
            return left
        return min(left, right)

    @staticmethod
    def transform_edge_list(edges, n):
        edges_list = [[] for _ in range(n)]
        for left, right in edges:
            edges_list[left].append(right)
        return edges_list

    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        redEdges = self.transform_edge_list(redEdges, n)
        blueEdges = self.transform_edge_list(blueEdges, n)

        def get_paths(is_red: bool):
            paths = [blueEdges, redEdges]
            return paths[is_red]

        shortest_paths = [[-1, -1] for _ in range(n)]
        visited = set()
        q = deque()

        for is_red in (True, False):
            visited.add((0, is_red))
            q.append((0, 0, is_red))

        while len(q) > 0:
            node, shortest_path, is_red = q.popleft()
            current_shortest = shortest_paths[node][is_red]
            if current_shortest != -1:
                shortest_path = min(shortest_path, current_shortest)
            shortest_paths[node][is_red] = shortest_path

            paths = get_paths(is_red)
            neighbours = paths[node]
            for neigbour in neighbours:
                if (neigbour, not is_red) in visited:
                    continue
                visited.add((neigbour, not is_red))
                q.append((neigbour, shortest_path + 1, not is_red))
    
        return list(map(self.positive_min, shortest_paths))