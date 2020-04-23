import pytest


class TestString:

    def __init__(self, text1, text2):
        self.text1 = text1
        self.text2 = text2

    def hello(self, name, date):
        return f"Hello {name}. Today is {date}"


@pytest.fixture
def string_fixture():
    return TestString(text1="HELLO".lower(), text2=str)


@pytest.fixture(params=("New User!", "Robert!", "Everyone!"))
def greeting_fixture(request):
    return request.param


@pytest.fixture
def set_fixture():
    s1 = {"java", "python", "c#", "ruby"}
    return s1


@pytest.fixture
def dict_fixture():
    d1 = {}
    return d1


@pytest.fixture
def dict2_fixture():
    d2 = {'brand': 'Mercedes-Benz', 'model': '300 SL', 'year': 1961}
    return d2
