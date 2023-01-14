import pytest
from goal_parser_interpretation import Solution


@pytest.mark.parametrize('command, expected', [
    ("G()(al)", "Goal"),
    ("G()()()()(al)", "Gooooal"),
    ("(al)G(al)()()G", "alGalooG"),
])
def test_solution(command, expected):
    assert Solution().interpret(command) == expected
