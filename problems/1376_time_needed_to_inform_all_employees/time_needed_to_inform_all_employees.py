from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinates = {}
        for idx, mngr in enumerate(manager):
            subordinates[mngr] = subordinates.get(mngr, []) + [idx]
        
        def inform_time(mngr: int):
            sub_inform_time = [inform_time(sub) for sub in subordinates.get(mngr, [])]
            return informTime[mngr] + max(sub_inform_time) if sub_inform_time else 0
        
        return inform_time(headID)