from typing import List
from collections import deque

class Solution:
    @staticmethod
    def neigbours(combination: str) -> List[str]:
        combinations = []
        for i in range(4):
            digit = int(combination[i])
            combinations.append(combination[:i] + str((digit + 1) % 10) + combination[i + 1:])
            combinations.append(combination[:i] + str((digit - 1) % 10) + combination[i + 1:])
        return combinations

    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)

        visited = set()
        q = deque()
        visited.add('0000')
        q.append(('0000', 0))
        while len(q) > 0:
            combination, steps = q.popleft()
            if combination == target:
                return steps
            
            if combination in deadends:
                    continue
            
            for neigbour in self.neigbours(combination):
                if neigbour in visited:
                    continue
                
                visited.add(neigbour)
                q.append((neigbour, steps + 1))
        return -1

