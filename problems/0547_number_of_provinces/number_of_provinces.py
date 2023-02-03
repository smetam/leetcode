from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n_cities = len(isConnected)
        visited = set()
        def dfs(start_city: int):
            q = [start_city]
            visited.add(start_city)
            while len(q) > 0:
                city = q.pop()
                for neighbour, is_connected in enumerate(isConnected[city]):
                    if neighbour in visited:
                        continue

                    if is_connected:
                        visited.add(neighbour)
                        q.append(neighbour)

        n_provinces = 0
        for city in range(n_cities):
            if city in visited:
                continue

            dfs(city)
            n_provinces += 1
        return n_provinces


class Solution1:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n_cities = len(isConnected)
        city2province = {x: x for x in range(n_cities)}
        for row in range(0, n_cities - 1):
            for col in range(row + 1, n_cities):
                is_connected = isConnected[row][col]
                if not is_connected:
                    continue
                
                province1 = city2province[row]
                province2 = city2province[col]
                if province1 == province2:
                    continue

                for city, province in city2province.items():
                    if province == province2:
                        city2province[city] = province1
        
        return len(set(city2province.values()))
                