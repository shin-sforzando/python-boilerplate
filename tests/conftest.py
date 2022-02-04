import pytest
from _pytest.logging import LogCaptureFixture

from logger import get_logger


@pytest.fixture
def caplog(caplog: LogCaptureFixture):
    logger = get_logger()
    handler_id = logger.add(caplog.handler, format="{message}")
    yield caplog
    logger.remove(handler_id)
