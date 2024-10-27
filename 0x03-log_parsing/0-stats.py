#!/usr/bin/python3
"""Module for logging metrics to stdout."""
import sys
import re
import signal


file_size = 0
status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }
count = 0


def print_stats():
    """Function to print the accumulated statistics."""
    print(f"File size: {file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def signal_handler(signum, frame):
    """Handler for keyboard interrupt."""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

pattern = (
    r'([\d]+\.[\d]+\.[\d]+\.[\d]+) - '
    r'\[[\d]{4}-[\d]{2}-[\d]{2} [\d]{2}:[\d]{2}:[\d]{2}\.[\d]{2,}\] '
    r'"GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)'
)

for line in sys.stdin:
    match = re.match(pattern, line)
    if match:
        status_code, size = match.groups()[1], match.groups()[2]
        file_size += int(size)
        if status_code in status_codes:
            status_codes[status_code] += 1
        count += 1
    if count == 10:
        print_stats()
        count = 0

print_stats()
