from loguru import logger


def get_logger():
    """Returns a standardized loguru logger

    Returns:
        loguru.logger.Logger: Initial settings have been applied.
    """

    logger.add("logs/{time}.log", rotation="24h")
    return logger
