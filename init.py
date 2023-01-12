import pathlib
import sys

TEST_TEMPLATE = """import pytest
from {name} import Solution


@pytest.mark.parametrize('nums, expected', [
    (1, 2),
    (3, 4),
])
def test_solution(nums, expected):
    assert Solution().solve(nums) == expected
"""


if __name__ == '__main__':
    arg = sys.argv[1]
    # problem id with leading zeores, example: "0035"
    problem_id, problem_name = arg.split('.')
    problem_id = problem_id.zfill(4)
    problem_name = (
        problem_name[1:]
        .lower()
        .replace(' ', '_')
        .replace('-', '_')
        .replace("'", '')
    )
    # problem_name = ''.join(c if c.isalnum() else '_' for c in problem_name)
    problem = f'{problem_id}_{problem_name}'
    
    path = pathlib.Path(__file__).parent / 'problems' / problem
    if path.exists():
        print("Already exists!")
    else:
        path.mkdir(exist_ok=True)
        with open(path / f'{problem_name}.py', 'w') as f:
            f.write("from typing import List\n\n\n")
        
        with open(path / f'test_{problem_name}.py', 'w') as f:
            f.write(TEST_TEMPLATE.format(name=problem_name))

    print(f'pytest problems/{problem}')