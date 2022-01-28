#!/usr/bin/env python3

import http.server

from logger import get_logger, logger_timing

HOST: str = "0.0.0.0"
"""str: Listening Host."""
PORT: int = 8000
"""int: Listening Port."""

Handler = http.server.SimpleHTTPRequestHandler
logger = get_logger()


@logger_timing()
def main() -> None:
    """Main function.

    Returns:
        None: This is the entry point.
    """
    with http.server.HTTPServer((HOST, PORT), Handler) as httpd:
        logger.info(f"Listening on {HOST}:{PORT} ...")
        logger.info(httpd.serve_forever())


if __name__ == "__main__":
    main()
