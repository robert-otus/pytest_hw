import pytest


def test_new_elements(dict_fixture):
    dict_fixture.update(([('brand', 'Mercedes-Benz'), ('model', '300 SL'), ('year', 1961)]))
    print(dict_fixture)


def test_adding_an_element(dict2_fixture):
    dict2_fixture["color"] = "silver"
    print(dict2_fixture)


def test_value_check(dict2_fixture):
    for x in dict2_fixture.values():
        print(x)


def test_value_change(dict2_fixture):
    dict2_fixture["year"] = 1959
    assert dict2_fixture["year"] == 1959


@pytest.mark.parametrize('cars', [{'brand': 'Volkswagen', 'model': 'Beetle', 'year': 1963},
                                 {"brand": "Ford", "model": "Mustang", "year": 1966},
                                 {"brand": "Porsche", "model": "911", "year": 1967}])
def test_year_compare(cars, dict2_fixture):
    dict2_fixture.update([('brand', 'Ferrari'), ('model', '250 GT California'), ('year', 1957)])
    assert cars["year"] >= dict2_fixture['year']

