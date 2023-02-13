from typing import List


class Solution:
    @staticmethod
    def transform_connections(connections, n):
        connected = [[] for _ in range(n)]
        for node_from, node_to in connections:
            forward = True
            connected[node_from].append((node_to, forward))
            forward = False
            connected[node_to].append((node_from, forward))
        return connected

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        connected = self.transform_connections(connections, n)
        reversions = 0
        visited = set()
        visited.add(0)

        q = [0]
        while len(q) > 0:
            city = q.pop()

            for connected_city, forward in connected[city]:
                if connected_city in visited:
                    continue
                visited.add(connected_city)
                if forward:
                    reversions += 1
                q.append(connected_city)
        return reversions
