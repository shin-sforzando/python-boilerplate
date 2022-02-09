import pytest

from src import get_logger


@pytest.fixture
def logger():
    return get_logger()
