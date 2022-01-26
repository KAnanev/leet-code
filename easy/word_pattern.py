# https://leetcode.com/problems/word-pattern/

def word_pattern(pattern: str, s: str) -> bool:
    f = lambda x: map({}.setdefault, x, range(len(x)))
    return list(f(pattern)) == list(f(s.split()))


def test_word_pattern():
    assert word_pattern('abba', 'dog cat cat dog')
    assert not word_pattern('abba', 'dog cat cat fish')
    assert not word_pattern('aaaa', 'dog cat cat dog')
