#!/usr/bin/python3
"""Module for logging some data to stdout"""
import sys
import re
import signal


def after_10():
    """Function to run every 10 headers or after a signal interrupt."""
    print(f"File size: {file_size}")
    for s, c in statuses.items():
        if c > 0:
            print(f"{s}: {c}")


def handle_exit(signum, frame):
    """Handle exit signals by running after_10 and then exiting."""
    after_10()
    sys.exit(0)


if __name__ == "__main__":
    statuses = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }
    file_size = 0
    count = 0
    signal.signal(signal.SIGINT, handle_exit)
    signal.signal(signal.SIGPIPE, handle_exit)

    while True:
        try:
            text = sys.stdin.readline()
            if not text:
                after_10()
                break
            pattern = (
                r'([\d]+\.[\d]+\.[\d]+\.[\d]+) - '
                r'\[[\d]{4}-[\d]{2}-[\d]{2} '
                r'[\d]{2}:[\d]{2}:[\d]{2}\.[\d]{2,}\] '
                r'"GET \/projects\/260 HTTP\/1\.1" '
                r'[\d]{3} '
                r'[\d]{1,4}'
            )
            splitted = text.split()
            match = re.search(pattern, text)
            if match is not None:
                file_size += int(splitted[-1])
                statuses[splitted[-2]] += 1
                if count == 10:
                    after_10()
                    count = 0
        except KeyboardInterrupt:
            handle_exit(None, None)

        count += 1
