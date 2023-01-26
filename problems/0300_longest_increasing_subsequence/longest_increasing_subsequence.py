from typing import List
import bisect


# O(n log(n)) time, O(n) space
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = []
        for num in nums:
            if len(seq) == 0 or seq[-1] < num:
                seq.append(num)
            else:
                # find idx of first elem >= num
                idx = bisect.bisect_left(seq, num)
                # replace it with num
                seq[idx] = num
        return len(seq)



# O(n ^ 2) time, O(n) space
class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = {}
        for num in nums:
            max_len = 1
            for last_elem, seq_len in seq.items():
                if last_elem == num:
                    new_len = seq_len
                elif last_elem < num:
                    new_len = seq_len + 1
                else: 
                    continue
                if new_len > max_len:
                    max_len = new_len
                
            seq[num] = max_len
        return max(seq.values())