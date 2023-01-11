from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater_number = {}
        stack = []
        for num in nums2:
            while len(stack) > 0 and stack[-1] < num:
                previous = stack.pop()
                greater_number[previous] = num
            stack.append(num)

        for elem in stack:
            greater_number[elem] = -1
        
        return list(map(lambda x: greater_number.get(x, -1), nums1))