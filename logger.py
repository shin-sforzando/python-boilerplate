import functools
import time

from loguru import logger
from tqdm import tqdm


def get_logger(file_prefix: str = "", file_postfix: str = "") -> logger:
    """Return a standardized loguru logger.

    Args:
        file_prefix (str, optional): File name prefix. Defaults to "".
        file_postfix (str, optional): File name postfix. Defaults to "".

    Returns:
        logger: With initial settings.
    """
    logger.remove()
    file_prefix = f"{file_prefix}{'_' if file_prefix else ''}"
    file_postfix = f"{'_' if file_postfix else ''}{file_postfix}"
    logger.add(f"logs/{file_prefix}{{time:YYYYMMDD}}{file_postfix}.log", rotation="24h")
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
