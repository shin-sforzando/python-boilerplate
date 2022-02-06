import logger


def test_get_logger():
    """Make sure that an instance of the logger is returned."""
    assert logger.get_logger()
