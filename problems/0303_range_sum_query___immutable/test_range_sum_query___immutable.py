import pytest
from range_sum_query___immutable import NumArray



def test_num_array_one():
    arr = NumArray([-2, 0, 3, -5, 2, -1])
    assert arr.sumRange(0, 2) == 1
    assert arr.sumRange(2, 5) == -1
    assert arr.sumRange(0, 5) == -3


def test_num_array_two():
    arr = NumArray([1, 3, 5])
    assert arr.sumRange(0, 2) == 9
    assert arr.sumRange(0, 0) == 1