#!/usr/bin/env python3

import http.server

from logger import get_logger

HOST: str = "0.0.0.0"
"""str: Listening Host."""
PORT: int = 8000
"""int: Listening Port."""

Handler = http.server.SimpleHTTPRequestHandler
logger = get_logger()


def main() -> None:
    """Main function.

    Returns:
        None: This is the entry point.
    """

    logger.debug("This is main().")
    with http.server.HTTPServer(("0.0.0.0", PORT), Handler) as httpd:
        logger.info(f"Listening on {HOST}:{PORT}")
        try:
            logger.info(httpd.serve_forever())
        except KeyboardInterrupt as ki:
            logger.warning(ki)


if __name__ == "__main__":
    main()
