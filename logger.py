from loguru import logger
from tqdm import tqdm


def get_logger():
    """Returns a standardized loguru logger

    Returns:
        loguru.logger.Logger: Initial settings have been applied.
    """

    logger.remove()
    logger.add("logs/{time}.log", rotation="24h")
    logger.add(lambda msg: tqdm.write(msg, end=""), colorize=True)
    return logger
