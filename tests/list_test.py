import pytest
from fibonacci import fibo


@pytest.mark.parametrize(
    'n, res', [(0, 0),
               (1, 1),
               (2, 1),
               (3, 2),
               (4, 3),
               (5, 5),
               (6, 8),
               (7, 13)])
def test_fib(n, res):
    assert fibo(n) == res


@pytest.fixture
def first_fixture():
    l1 = ["one", "two", "three"]
    return l1


def test_compare(first_fixture):
    l2 = ["one", "two", "three"]
    assert first_fixture == l2


def test_length(first_fixture):
    l2 = []
    for i in range(3):
        l2.append(i)
    assert len(first_fixture) == len(l2)



