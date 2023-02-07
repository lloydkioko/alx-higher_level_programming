#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, encoing='utf-8') as f:
        print(f.read(), end="")
