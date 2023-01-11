from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        prev_x, prev_y = coordinates[0]
        curr_x, curr_y = coordinates[1]
        dx = curr_x-prev_x
        dy = curr_y-prev_y
        angle = None
        if dx != 0:
            angle = dy / dx 
        for x, y in coordinates[2:]:
            if x - curr_x == 0:
                if dx != 0:
                    return False
                else:
                    continue
            
            new_angle = (y - curr_y) / (x-curr_x)
            if new_angle != angle:
                return False
            curr_x, curr_y = x, y
        return True