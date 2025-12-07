import pytest
# Update this line to include 'power'
from calculator import add, subtract, multiply, divide, power


@pytest.mark.basic
def test_add():
    """Test addition function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


@pytest.mark.basic
def test_subtract():
    """Test subtraction function."""
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(-3, -2) == -1


@pytest.mark.basic
def test_multiply():
    """Test multiplication function."""
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0


@pytest.mark.basic
def test_divide():
    """Test division function."""
    assert divide(8, 2) == 4
    assert divide(9, 3) == 3
    assert divide(-10, 2) == -5


@pytest.mark.edge
def test_divide_by_zero():
    """Test that dividing by zero raises an error."""
    with pytest.raises(ValueError):
        divide(10, 0)


@pytest.mark.basic
def test_power():
    """Test power function."""
    assert power(2, 3) == 8      # 2^3 = 8
    assert power(5, 0) == 1      # x^0 = 1
    assert power(3, 2) == 9      # 3^2 = 9


@pytest.mark.slow
def test_large_calculations():
    """Test performance with larger numbers."""
    result = multiply(999999, 999999)
    assert result == 999998000001
    assert add(1000000, 2000000) == 3000000
    assert power(10, 6) == 1000000


@pytest.mark.edge
def test_negative_power():
    """Test edge case with negative exponents."""
    assert power(2, -1) == 0.5
    assert power(10, -2) == 0.01