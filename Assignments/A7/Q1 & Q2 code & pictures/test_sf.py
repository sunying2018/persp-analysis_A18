import sf
import pytest


def test_smallest_factor():
    assert sf.smallest_factor(1) == 1, "failed on 1"
    assert sf.smallest_factor(2) == 2, "failed on 2"
    assert sf.smallest_factor(3) == 3, "failed on 3"
    assert sf.smallest_factor(4) == 2, "failed on 4"
    assert sf.smallest_factor(5) == 5, "failed on 5"
    assert sf.smallest_factor(6) == 2, "failed on 6"
    assert sf.smallest_factor(7) == 7, "failed on 7"
    assert sf.smallest_factor(11) == 11, "failed on 11"
    assert sf.smallest_factor(100) == 2, "failed on 100"