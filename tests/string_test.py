import pytest


def test_hello(string_fixture):
    assert string_fixture.hello("Robert", "April 21") == "Hello Robert. Today is April 21"


def test_word(string_fixture):
    assert string_fixture.text1 + " " + "world" == "hello world"


def test_reverse(string_fixture):
    text3 = "dlrow"
    assert string_fixture.text2("World") == text3[::-1].capitalize()


def test_num(string_fixture):
    assert string_fixture.text2(123) == "123"


@pytest.mark.parametrize("greet", ("Hello", "Bye"))
def test_greeting(greet, greeting_fixture):
   print(greet, greeting_fixture)


