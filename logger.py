import functools
import time

from loguru import logger
from tqdm import tqdm


def get_logger():
    """Return a standardized loguru logger.

    Returns:
        loguru.logger.Logger: Initial settings have been applied.
    """

    logger.remove()
    logger.add("logs/{time}.log", rotation="24h")
    logger.add(lambda msg: tqdm.write(msg, end=""), colorize=True)
    return logger


def logger_timing(*, entering=True, leaving=True, timeit=True, level="DEBUG"):
    """Wrapper for additional output about timing.

    Args:
        entering (bool): Whether or not to output the entry time.
        leaving (bool): Whether or not to output the leaving time.
        timeit (bool): Whether or not to output the processing time.
        level (str): Level of additional output.

    Returns:
        wrapper: A Decorator.

    Note:
        https://loguru.readthedocs.io/en/stable/resources/recipes.html
    """

    def wrapper(func):
        name = func.__name__

        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            _logger = logger.opt(depth=1)
            if timeit:
                start = time.time()
            if entering:
                _logger.log(level, f"Entering: '{name}' (args={args}, kwargs={kwargs})")
            result = func(*args, **kwargs)
            if timeit:
                elapsed_time = time.time() - start
            if leaving:
                _logger.log(level, f"Exiting: '{name}' (result={result})")
            if timeit:
                logger.debug(f"Function '{name}' executed in {elapsed_time:f} [s]")
            return result

        return wrapped

    return wrapper
