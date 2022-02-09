import pytest

from src import main


def test_simple():
    """Make sure the equation is always valid."""
    assert 1 + 1 == 2


def test_zero_division():
    """Make sure the exceptions are raised."""
    with pytest.raises(ZeroDivisionError):
        1 / 0


def test_main():
    """Make sure that there is a main() in src/main.py."""
    assert hasattr(main, "main")


def test_with_mock(mocker):
    """Test with Mock.

    Args:
        mocker (Mock): src/main.py main().
    """

    def always_return_true():
        return True

    assert mocker.patch("src.main.main", side_effect=always_return_true)
