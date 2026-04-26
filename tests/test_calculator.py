# tests will be added in PR #2 when functions are implemented
from src.calculator import add, subtract
def test_add():
    assert add(2, 3) == 5

def test_substract():
    assert subtract(4,2) == 2