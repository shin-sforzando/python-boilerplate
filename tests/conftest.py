import pytest
from _pytest.logging import LogCaptureFixture

from logger import get_logger


@pytest.fixture
def caplog(caplog: LogCaptureFixture):
    """Caplog fixture to be used with loguru.

    Args:
        caplog (LogCaptureFixture): Provides access and control of log capturing.

    Yields:
        caplog: The fixture to capture logging output.

    Note:
        cf. https://bit.ly/3rwdyY2
    """
    logger = get_logger()
    handler_id = logger.add(caplog.handler, format="{message}")
    yield caplog
    logger.remove(handler_id)
