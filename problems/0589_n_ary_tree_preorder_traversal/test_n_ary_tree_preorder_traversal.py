import pytest
from n_ary_tree_preorder_traversal import Solution, list_to_tree



@pytest.mark.parametrize('root, expected', [
    ([1,None,3,2,4,None,5,6], [1,3,5,6,2,4]),
    ([1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14], [1,2,3,6,7,11,14,4,8,12,5,9,13,10]),
])
def test_solution(root, expected):
    assert Solution().preorder(list_to_tree(root)) == expected
