import pytest
from populating_next_right_pointers_in_each_node import Solution, Node


def get_expected():
    nodes = {i: Node(val=i) for i in range(1, 8)}
    
    nodes[1].left = nodes[2]
    nodes[1].right = nodes[3]

    nodes[2].left = nodes[4]
    nodes[2].right = nodes[5]

    nodes[3].left = nodes[6]
    nodes[3].right = nodes[7]

    nodes[2].next = nodes[3]
    nodes[4].next = nodes[5]
    nodes[5].next = nodes[6]
    nodes[6].next = nodes[7]
    return nodes[1]

def get_input():
    nodes = {i: Node(val=i) for i in range(1, 8)}
    
    nodes[1].left = nodes[2]
    nodes[1].right = nodes[3]

    nodes[2].left = nodes[4]
    nodes[2].right = nodes[5]

    nodes[3].left = nodes[6]
    nodes[3].right = nodes[7]
    return nodes[1]


@pytest.mark.parametrize('root, expected', [
    (get_input(), get_expected()),
    (Node(val=1), Node(val=1))
])
def test_solution(root, expected):
    assert Solution().connect(root) == expected
