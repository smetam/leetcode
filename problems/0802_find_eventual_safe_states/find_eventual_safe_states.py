from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe_nodes = []

        n = len(graph)
        incoming_nodes = [[] for _ in range(n)]
        outcoming_count = {}
        q = []
        for node_from, adj in enumerate(graph):
            n_outcoming = len(adj)
            if n_outcoming == 0:
                q.append(node_from)
            else:
                outcoming_count[node_from] = n_outcoming
            for node_to in adj:
                incoming_nodes[node_to].append(node_from)
        
        while len(q) > 0:
            node = q.pop()
            safe_nodes.append(node)
            for incoming in incoming_nodes[node]:
                n_outcoming = outcoming_count[incoming]
                n_outcoming -= 1
                if n_outcoming == 0:
                    q.append(incoming)
                    outcoming_count.pop(incoming)
                else:
                    outcoming_count[incoming] = n_outcoming
        return sorted(safe_nodes)