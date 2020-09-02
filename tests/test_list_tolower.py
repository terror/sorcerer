from sorcerer.utils import list_tolower


def test_list_tolower():
    tests = [
        (["AbC", "aBc", "abc"], ["abc", "abc", "abc"]),
        (["XyZ", "OOOO", "zZzZz"], ["xyz", "oooo", "zzzzz"]),
        (["A", "b", "c", "D"], ["a", "b", "c", "d"])
    ]
    for k, v in tests:
        assert(list_tolower(k) == v)
