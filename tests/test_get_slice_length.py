from sorcerer.utils import get_slice_length


def test_get_slice_length():
    paths = {
        "../../example": 6,
        "../example": 3,
        "../../../example": 9
    }
    for k, v in paths.items():
        assert(get_slice_length(k) == v)
