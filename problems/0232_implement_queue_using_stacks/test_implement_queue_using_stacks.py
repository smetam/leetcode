import pytest
from implement_queue_using_stacks import MyQueue


def test_solution_one():
    q = MyQueue()
    q.push(1)
    q.push(2)
    assert q.peek() == 1
    assert q.pop() == 1
    assert q.empty() is False



def test_solution_two():
    q = MyQueue()
    q.push(1)
    assert q.peek() == 1
    assert q.empty() is False