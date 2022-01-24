import http.server

from logger import get_logger

PORT: int = 8000
"""int: Listening Port"""

Handler = http.server.SimpleHTTPRequestHandler
logger = get_logger()


def main():
    """Main function"""
    logger.debug("This is main().")
    with http.server.HTTPServer(("0.0.0.0", PORT), Handler) as httpd:
        logger.info(f"Listening Port: {PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt as ki:
            logger.info(ki)


if __name__ == "__main__":
    main()
