#!/usr/bin/env python3
import time
import sys

sys.stdout.write("loading: ")
# print("loading: ", end="\n")
while True:
    for i in ['/', '-', '\\', '|']:
        # print(i, end='')
        sys.stdout.write(50*i)
        # sys.stdout.write(i)
        # sys.stdout.write(i)
        # sys.stdout.write(i)
        # sys.stdout.write(i)
        # sys.stdout.write(i)
        # sys.stdout.write(i)
        # sys.stdout.write(i)
        time.sleep(0.1)
        sys.stdout.write(50*"\b")
        # sys.stdout.write("\b")
        # sys.stdout.write("\b")
        # sys.stdout.write("\b")
        # sys.stdout.write("\b")
        # sys.stdout.write("\b")
        # sys.stdout.write("\b")
        # sys.stdout.write("\b")
        sys.stdout.flush()
