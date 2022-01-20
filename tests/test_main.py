import pytest

import main


def test_simple():
    assert 1 + 1 == 2


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0


def test_main():
    assert hasattr(main, "main")


def test_with_mock(mocker):
    def always_return_true():
        return True

    assert mocker.patch("main.main", side_effect=always_return_true)
