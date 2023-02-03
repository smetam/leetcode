from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        n_cables = len(connections)
        if n_cables < n - 1:
            # not enough cables
            return -1
        
        conn = [[] for _ in range(n)]
        for left, right in connections:
            conn[left].append(right)
            conn[right].append(left)
    
        visited = set()

        def dfs(start: int):
            q = [start]
            visited.add(start)
            while len(q) > 0:
                node = q.pop()
                for neighbour in conn[node]:
                    if neighbour in visited:
                        continue

                    visited.add(neighbour)
                    q.append(neighbour)
        
        n_nets = 0
        for node in range(n):
            if node in visited:
                continue

            dfs(node)
            n_nets += 1
        
        return n_nets - 1
