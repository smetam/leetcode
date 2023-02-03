from typing import List


class Solution:
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
                