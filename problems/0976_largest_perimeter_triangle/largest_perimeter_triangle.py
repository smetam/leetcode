from typing import List
import heapq

class Solution:
    @staticmethod
    def is_valid_triangle(a: int, b: int, c: int) -> bool:
        return (a + b > c) and (b + c > a) and (a + c > b)

    def largestPerimeter(self, nums: List[int]) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        a, b, c = -heapq.heappop(nums), -heapq.heappop(nums), -heapq.heappop(nums)
        while (not self.is_valid_triangle(a, b, c)) and (len(nums) > 0):
            a, b, c = b, c, -heapq.heappop(nums)

        if self.is_valid_triangle(a, b, c):
            return a + b + c
        return 0        


        
