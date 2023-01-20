import pytest
from word_break import Solution


@pytest.mark.parametrize('s, wordDict, expected', [
    ("leetcode", ["leet","code"], True),
    ("applepenapple", ["apple","pen"], True),
    ("catsandog", ["cats","dog","sand","and","cat"], False),
    ("a" * 200 + "b", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"], False),
])
def test_solution(s, wordDict, expected):
    assert Solution().wordBreak(s, wordDict) == expected
