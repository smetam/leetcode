from typing import List


# compute rolling sum on creation
class NumArray:

    def __init__(self, nums: List[int]):
        self.rolling_sum = [0]
        acc = 0
        for num in nums:
            acc += num
            self.rolling_sum.append(acc)

    def sumRange(self, left: int, right: int) -> int:
        return self.rolling_sum[right+1] - self.rolling_sum[left]

# compute sum when needed
class NumArray1:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left: right + 1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)