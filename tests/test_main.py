from app.main import greet


def test_greet_default():
    assert greet() == "Hello from repair"


def test_greet_custom():
    assert greet("x") == "Hello from x"
