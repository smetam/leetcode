from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_distance = -1
        min_idx = -1
        for idx, point in enumerate(points):
            point_x, point_y = point
            if x == point_x:
                distance = abs(y - point_y)
            elif y == point_y:
                distance = abs(x - point_x)
            else:
                continue
            if (min_distance == -1) or (distance < min_distance):
                min_distance = distance
                min_idx = idx
        return min_idx
                
            