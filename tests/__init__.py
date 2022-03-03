import pytest

from src import get_logger


@pytest.fixture
def logger():
    """Fixture for logger.

    Returns:
        loguru.logger: As test logger.
    """
    return get_logger()
