class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_position = {}
        max_len = 0
        current_len = 0
        for idx, c in enumerate(s):
            last_c_idx = last_position.get(c, -1)
            current_len = min(idx - last_c_idx, current_len + 1)
            if current_len > max_len:
                max_len = current_len
            last_position[c] = idx
        return max_len