import pytest
from _pytest.logging import LogCaptureFixture


@pytest.fixture
def caplog(logger, caplog: LogCaptureFixture):
    """Caplog fixture to be used with loguru.

    Args:
        logger: Logger.
        caplog (LogCaptureFixture): Provides access and control of log capturing.

    Yields:
        caplog: The fixture to capture logging output.

    Note:
        cf. https://bit.ly/3rwdyY2
    """
    handler_id = logger.add(caplog.handler, format="{message}")
    yield caplog
    logger.remove(handler_id)
