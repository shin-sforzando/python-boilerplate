import http.server

from logger import get_logger

PORT: int = 8000
"""int: Listening Port"""

Handler = http.server.SimpleHTTPRequestHandler
logger = get_logger()


def main():
    """Main function"""
    logger.debug("This is main().")
    with http.server.HTTPServer(("", PORT), Handler) as httpd:
        print(f"Listening Port: {PORT}")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
