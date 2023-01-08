from typing import List

# O(1) space
class Solution:
    # start is inclusive, end is not
    @staticmethod
    def reverse(nums, start, end): 
        end -= 1      
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # if k > n we don't need to rotatate that many times
        k = k % n
        self.reverse(nums, 0, n - k)
        self.reverse(nums, n - k, n)
        self.reverse(nums, 0, n)
        

# O(n) space
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         if n < 2: 
#             return
#         rotate_queue = set(range(n))
#         # if k > n we don't need to rotatate that many times
#         k = k % n
#         elem, idx = None, None
#         while len(rotate_queue) > 0:
#             if idx is None:
#                 idx = rotate_queue.pop()
#                 elem = nums[idx]
#             else:
#                 rotate_queue.remove(idx)
#             new_idx = (idx + k) % n
#             if new_idx not in rotate_queue:
#                 nums[new_idx] = elem
#                 elem, idx = None, None
#             else:
#                 new_elem = nums[new_idx]
#                 nums[new_idx] = elem
#                 elem, idx = new_elem, new_idx
