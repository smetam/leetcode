from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()
        q = [0]
        while len(q) > 0:
            room = q.pop()
            visited.add(room)
            keys = rooms[room]
            for key in keys:
                if key not in visited:
                    q.append(key)
        return len(visited) == n