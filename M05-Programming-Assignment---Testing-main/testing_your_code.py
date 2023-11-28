import pytest


def test_sum():
    """should be 6"""
    assert sum([1, 2, 3]) == 6


def test_sum_tuple():
    """should be 6, but its 5"""
    assert sum((1, 2, 2)) == 6


if __name__ == '__main__':
    pytest.main([__file__])