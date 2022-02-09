import functools
import time
from typing import Union

from loguru import logger
from tqdm import tqdm


def get_logger(
    file_prefix: str = "", file_postfix: str = "", level: Union[str, int] = "DEBUG"
) -> logger:
    """[summary]

    Args:
        file_prefix (str, optional): Prefix of log file. Defaults to "".
        file_postfix (str, optional): Postfix of log file. Defaults to "".
        level (Union, optional): Level threshold. Defaults to "DEBUG".

    Returns:
        logger: With configuration.
    """
    logger.remove()
    file_prefix = f"{file_prefix}{'_' if file_prefix else ''}"
    file_postfix = f"{'_' if file_postfix else ''}{file_postfix}"
    logger.add(
        f"logs/{file_prefix}{{time:YYYYMMDD}}{file_postfix}.log",
        rotation="24h",
        level=level,
    )
    logger.add(lambda msg: tqdm.write(msg, end=""), colorize=True, level=level)
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


logger = get_logger()
logger.debug("src/__init__.py")
