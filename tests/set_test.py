import pytest
import random


def test_unite(set_fixture):
    s2 = {"javascript", "java", "c++", "swift", "python"}
    su = s2.union(set_fixture)
    print(su)


def test_diff(set_fixture):
    s2 = {"javascript", "java", "c++", "swift", "python"}
    su = s2.difference(set_fixture)
    print(su)


def test_length(set_fixture):
    assert len(set_fixture) == 4


def test_duplicates(set_fixture):
    for i in range(3):
        set_fixture.add("python")
    assert len(set_fixture) == 4


@pytest.mark.parametrize("sets", ({1, 4, 3, 2, 5, 7, 6},
                                  {2, 6, 1, 3, 0},
                                  {0, 1, 2, 3, 4, 5, 6, 7},
                                  {5, 1, 4, 6, 2}))
def test_numbers(sets):
    rand = random.sample(range(8), 3)
    my_set = set(rand)
    print(my_set)
    assert my_set.issubset(sets) == True


